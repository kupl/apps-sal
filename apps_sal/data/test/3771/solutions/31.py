import sys
sys.setrecursionlimit(1000000)


def FF(E, s, t):
    NN = H + W + 2
    G = [[] for _ in range(NN)]
    for a, b, f in E:
        G[a].append([b, f, len(G[b])])
        G[b].append([a, 0, len(G[a]) - 1])

    def dfs(s, t, f):
        if s == t:
            return f
        used[s] = 1
        for i, (b, _f, r) in enumerate(G[s]):
            if used[b] or _f == 0: continue
            d = dfs(b, t, min(f, _f))
            if d > 0:
                G[s][i][1] -= d
                G[b][r][1] += d
                return d
        return 0

    flow = 0
    while 1:
        used = [0] * NN
        f = dfs(s, t, 10**100)
        if f == 0:
            return flow
        flow += f


E = []

H, W = list(map(int, input().split()))
for i in range(H):
    A = input()
    for j in range(W):
        if A[j] == "o":
            E.append((i, j + H, 1))
            E.append((j + H, i, 1))
        elif A[j] == "S":
            S = (i, j + H)
        elif A[j] == "T":
            T = (i, j + H)
E.append((H + W, S[0], 10**6))
E.append((H + W, S[1], 10**6))
E.append((T[0], H + W + 1, 10**6))
E.append((T[1], H + W + 1, 10**6))

ff = FF(E, H + W, H + W + 1)
print((ff if ff < 10**6 else -1))
