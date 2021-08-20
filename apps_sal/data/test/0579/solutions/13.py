from itertools import accumulate
import sys
sys.setrecursionlimit(10 ** 6)
(n, k) = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))


def dfs(G, v, p):
    seen[v] = True
    sc.append(c[v])
    for nv in G[v]:
        if nv == p:
            continue
        if seen[nv]:
            pos[0] = nv
            return
        dfs(G, nv, v)
        if pos[0] != -1:
            return


G = [[] for _ in range(n)]
for i in range(n):
    G[i].append(p[i] - 1)
seen = [False] * n
ans = -float('inf')
for i in range(n):
    if seen[i] == False:
        pos = [-1]
        sc = []
        dfs(G, i, -1)
        if sc:
            sumsc = sum(sc)
            lenc = len(sc)
            for j in range(lenc):
                if j != 0:
                    sc = sc[1:] + [sc[0]]
                ac = list(accumulate(sc))
                if sumsc <= 0:
                    ans = max(ans, max(ac[:min(k, lenc)]))
                elif k % lenc == 0:
                    ans = max(ans, ac[-1] * (k // lenc - 1) + max(ac))
                else:
                    ans = max(ans, ac[-1] * (k // lenc) + max(ac[:k % lenc]))
print(ans)
