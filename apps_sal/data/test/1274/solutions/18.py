from heapq import *
n, m = map(int, input().split())
ab = []
ans = [[] for i in range(m)]
aa = 0
for i in range(n):
    a, b = map(int, input().split())
    a -= 1
    b *= -1
    ab.append((a, b))
ab.sort()
t = []
heapify(t)
for a, b in ab:
    if a < m:
        ans[a].append(b)
for i in range(m):
    for j in ans[i]:
        heappush(t, j)
    if len(t) > 0:
        tt = heappop(t) * (-1)
        aa += tt
print(aa)
