import sys
sys.setrecursionlimit(10 ** 7)
(N, Q) = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
lst = []
for _ in range(Q):
    (P, X) = map(int, input().split())
    P -= 1
    lst.append((P, X))
cnt = [0] * N
for (p, x) in lst:
    cnt[p] += x
seen = [False] * N


def dfs(v):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v] == True:
            continue
        cnt[next_v] += cnt[v]
        dfs(next_v)


dfs(0)
print(*cnt)
