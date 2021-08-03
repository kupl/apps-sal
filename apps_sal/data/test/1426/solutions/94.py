import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edge = []
graph = [[] for i in range(n + 1)]
for i in range(m):
    edge.append(list(map(int, input().split())))
    graph[edge[-1][0]].append(edge[-1][1])
s, g = map(int, input().split())

INF = 10**18
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
