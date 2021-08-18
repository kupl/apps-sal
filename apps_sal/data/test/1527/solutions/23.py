from copy import deepcopy

H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
ans = 0
queue = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def now(n, s):
    t = []
    for i in queue:
        j = n[0] + i[0]
        k = n[1] + i[1]
        if 0 <= j < H and 0 <= k < W:
            if s[j][k] == ".":
                t.append([j, k])
                s[j][k] = "
    return [t, s]


def bfs(trust, a, s):
    t = []
    for i in trust:
        tt, s = now(i, s)
        t += tt
    if len(t) == 0:
        return a
    else:
        a = a + 1
        return bfs(t, a, s)


for i in range(H):
    for j in range(W):
        s = deepcopy(S)
        if S[i][j] == ".":
            s[i][j] = "
            ans = max(ans, bfs([[i, j]], 0, s))
print(ans)
