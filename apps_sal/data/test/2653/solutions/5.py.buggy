from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

n, q = list(map(int, input().split()))
G = [[] * n for i in range(n)]
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


done = [False] * n
points = [0] * n
d = defaultdict(lambda: 0)

for _ in range(q):
    a, b = list(map(int, input().split()))
    d[a - 1] += b


def dfs(i, cnt):
    cnt += d[i]
    points[i] += cnt
    done[i] = True
    for j in G[i]:
        if not done[j]:
            dfs(j, cnt)


dfs(0, 0)
print((*points))
