from collections import Counter
import sys
sys.setrecursionlimit(10 ** 6)


def dfs(nw):
    for nx in F[nw]:
        if V[nx] == -1:
            V[nx] = cnt
            dfs(nx)


(n, m, k) = list(map(int, sys.stdin.readline().split()))
F = [[] for _ in range(n)]
B = [[] for _ in range(n)]
for i in range(m):
    (a, b) = map(lambda x: int(x) - 1, map(int, sys.stdin.readline().split()))
    F[a].append(b)
    F[b].append(a)
for i in range(k):
    (c, d) = map(lambda x: int(x) - 1, map(int, sys.stdin.readline().split()))
    B[c].append(d)
    B[d].append(c)
V = [-1] * n
cnt = 1
for i in range(n):
    if V[i] == -1:
        V[i] = cnt
        dfs(i)
        cnt += 1
cV = Counter(V)
ans = []
for i in range(n):
    ans.append(cV[V[i]] - 1 - len(F[i]) - sum([V[b] == V[i] for b in B[i]]))
print(*ans)
