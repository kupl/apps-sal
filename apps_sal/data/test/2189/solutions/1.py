from heapq import heappush, heappop
def q(): return map(int, input().split())


n, m = q()
a = d = [0] * n
e = [[] for _ in range(n)]
h = []
while(m):
    l, r = q()
    d[l - 1] += 1
    e[r - 1] += [l - 1]
    m -= 1
for i in range(n):
    if(d[i] == 0):
        heappush(h, -i)
j = n
while(h):
    t = -heappop(h)
    a[t] = j
    j -= 1
    for x in e[t]:
        d[x] -= 1
        if(d[x] == 0):
            heappush(h, -x)
print(''.join(str(x) + ' ' for x in a))
