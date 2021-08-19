# https://codeforces.com/problemset/problem/770/C
n, k = list(map(int, input().split()))
K = set(list(map(int, input().split())))
g = {}
rg = {}
deg = {}


def push_d(deg, u, val):
    if u not in deg:
        deg[u] = 0
    deg[u] += val


def push_g(g, u, v):
    if u not in g:
        g[u] = []
    g[u].append(v)


for u in range(1, n + 1):
    list_v = list(map(int, input().split()))[1:]
    deg[u] = 0

    for v in list_v:
        push_d(deg, u, 1)
        push_g(g, v, u)
        push_g(rg, u, v)

S = [x for x in K]
used = [0] * (n + 1)
i = 0
while i < len(S):
    u = S[i]
    if u in rg:
        for v in rg[u]:
            if used[v] == 0:
                used[v] = 1
                S.append(v)
    i += 1

S = {x: 1 for x in S}
deg0 = [x for x in S if deg[x] == 0]
ans = []


def process(g, deg, deg0, u):
    if u in g:
        for v in g[u]:
            if v in S:
                push_d(deg, v, -1)

                if deg[v] == 0:
                    deg0.append(v)


while len(deg0) > 0 and len(K) > 0:
    u = deg0.pop()
    ans.append(u)

    if u in K:
        K.remove(u)

    process(g, deg, deg0, u)

if len(K) > 0:
    print(-1)
else:
    print(len(ans))
    print(' '.join([str(x) for x in ans]))

# 6 2
# 5 6
# 0
# 1 1
# 1 4 5
# 2 2 1
# 1 4
# 2 5 3
