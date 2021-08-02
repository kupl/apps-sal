from heapq import heappop, heappush

n, k = [int(x) for x in input().split()]
cs = []
for i in range(n):
    l, r = [int(x) for x in input().split()]
    cs.append((l, r, i + 1))
cs.sort()
h = []

for i in range(k - 1):
    heappush(h, [cs[i][1], cs[i][2]])
lcs = h[:]
l = -1
push_i = k - 1
for i in range(k - 1, n):
    heappush(h, [cs[i][1], cs[i][2]])
    d = h[0][0] - cs[i][0]
    if d > l:
        l = d
        if push_i != k - 1:
            heappop(lcs)
        for j in range(push_i, i):
            heappush(lcs, [cs[j][1], cs[j][2]])
            heappop(lcs)
        heappush(lcs, [cs[i][1], cs[i][2]])
        push_i = i + 1
    heappop(h)

print(l + 1)
if l == -1:
    for i in range(1, k + 1):
        print(i, end=' ')

else:
    for r, i in lcs:
        print(i, end=' ')
