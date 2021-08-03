from itertools import combinations

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
m = int(input())
uv = [list(map(int, input().split())) for _ in range(m)]

adj = [[] for _ in range(n)]
ids = [[-1] * n for _ in range(n)]
for i, (a, b) in enumerate(ab):
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)
    ids[a][b] = i
    ids[b][a] = i


def dfs(s, g):
    d = [-1] * n
    d[s] = 0
    p = [-1] * n
    stack = [s]

    while stack:
        u = stack.pop()
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                p[v] = u
                stack.append(v)

    v = g
    ret = 0
    while v != s:
        i = ids[v][p[v]]
        ret += 1 << i
        v = p[v]

    return ret


def bin_count(tpl):
    sm_or = 0
    for e in tpl:
        sm_or |= e

    return bin(sm_or).count("1")


path = [dfs(u - 1, v - 1) for u, v in uv]
ex = 0
for i in range(1, m + 1):
    for tpl in combinations(path, i):
        ex += pow(2, n - 1 - bin_count(tpl)) * (-1) ** (i % 2 + 1)

ans = pow(2, n - 1) - ex
print(ans)
