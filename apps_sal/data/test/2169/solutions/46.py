from collections import defaultdict

H, W, D = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

# 1 -> 1+D ->
# 2 -> 2+D ->
# 3 -> 3+D -> みたいなものを事前に計算

# 辞書で管理する
# d[A[i][j]] = [i,j] みたいな感じ
d = defaultdict(list)
for i in range(H):
    for j in range(W):
        d[A[i][j]].append([i, j])


p = []
for s in range(1, D + 1):
    c = 0
    q = [0]
    for i in range(s + D, H * W + 1, D):
        i0, j0 = d[i - D][0]
        i1, j1 = d[i][0]
        c += abs(i0 - i1) + abs(j0 - j1)
        q.append(c)

    p.append(q)


for l, r in LR:
    i = l % D - 1
    s = (l - 1) // D
    e = (r - 1) // D
    print((p[i][e] - p[i][s]))
