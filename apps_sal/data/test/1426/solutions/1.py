import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
s, g = map(int, input().split())

INF = 10**7
ans = [[INF, INF, INF] for i in range(n + 1)]
q = [s]
d = 0
while q:
    nq = []
    d += 1
    p = d % 3
    for cf in q:
        for ct in graph[cf]:
            if ans[ct][p] == INF:
                ans[ct][p] = d
                nq.append(ct)
    q = copy.deepcopy(nq)
if ans[g][0] == INF:
    print(-1)
else:
    print(ans[g][0] // 3)
