from heapq import *

n, m, s = map(int, input().split())
s = min([s, 50*n])
tree = [[] for _i in range(n+1)]
for _i in range(m):
    u, v, a, b = map(int, input().split())
    tree[u].append([v, a, b])
    tree[v].append([u, a, b])

cd = [[0,0]]
for _i in range(n):
    cd.append(list(map(int, input().split())))

dp = [[float('inf') for _i in range(50*n+1)] for _j in range(n+1)]
hq = [[0, 1, s]]
dp[1][s] = 0
heapify(hq)
while hq:
    t, p, g = heappop(hq)
    if g+cd[p][0] <= 50*n:
        x, y = t+cd[p][1], min([g+cd[p][0], 50*n])
        if dp[p][y] > x:
            dp[p][y] = x
            heappush(hq, [x, p, y])
    for x, y, z in tree[p]:
        if g-y >= 0 and dp[x][g-y] > t+z:
            dp[x][g-y] = t+z
            heappush(hq, [t+z, x, g-y])

for i in dp[2:]:
    print(min(i))
