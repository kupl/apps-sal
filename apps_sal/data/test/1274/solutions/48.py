from heapq import heapify, heappop, heappush
(n, m) = map(int, input().split())
l = [[] for i in range(10 ** 5)]
ans = 0
for i in range(n):
    (a, b) = map(int, input().split())
    l[a - 1].append(-b)
for i in range(10 ** 5):
    heapify(l[i])
p = []
heapify(p)
for i in range(m):
    if len(l[i]) != 0:
        heappush(p, [heappop(l[i]), i])
    if len(p) != 0:
        x = heappop(p)
        ans += -x[0]
        if len(l[x[1]]) != 0:
            heappush(p, [heappop(l[x[1]]), x[1]])
print(ans)
