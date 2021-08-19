N, K = map(int, input().split())
P = list(map(int, input().split()))
_c = list(map(int, input().split()))

# Cを書き換える
C = [0] * N
for i in range(N):
    P[i] -= 1
    C[i] = _c[P[i]]

m = 31  # bit数

# ダブリング
vertex = list()
score = list()
vertex.append(P)
score.append(C)
for b in range(1, m + 1):
    p_bth = [0] * N
    c_bth = [0] * N
    for i in range(N):
        p_bth[i] = vertex[b - 1][vertex[b - 1][i]]
        c_bth[i] = score[b - 1][i] + score[b - 1][vertex[b - 1][i]]
    vertex.append(p_bth)
    score.append(c_bth)

# 桁DP
MIN = -(1 << 63)
prv = [[MIN, 0] for _ in range(N)]
nxt = [[MIN, MIN] for _ in range(N)]
for b in range(m, -1, -1):
    for i in range(N):
        if (K >> b) & 1:
            nxt[vertex[b][i]][0] = max(nxt[vertex[b][i]][0], prv[i][0] + score[b][i])
            nxt[vertex[b][i]][1] = max(nxt[vertex[b][i]][1], prv[i][1] + score[b][i])
            nxt[i][0] = max(nxt[i][0], prv[i][0], prv[i][1])
        else:
            nxt[vertex[b][i]][0] = max(nxt[vertex[b][i]][0], prv[i][0] + score[b][i])
            nxt[i][0] = max(nxt[i][0], prv[i][0])
            nxt[i][1] = max(nxt[i][1], prv[i][1])
    prv, nxt = nxt, prv

ans = max(max(x) for x in prv)
if ans == 0:
    ans = max(C)

print(ans)
