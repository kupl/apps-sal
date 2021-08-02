H, W, D = list(map(int, input().split()))
A = []

for h in range(H):
    A.append(list(map(int, input().split())))

pos = {}
for h in range(H):
    for w in range(W):
        pos[A[h][w]] = [h, w]

S = [0] * (H * W)
for d in range(D):
    tmp = 0
    now = d + 1
    while now + D <= H * W:
        nowh, noww = pos[now]
        newh, neww = pos[now + D]
        tmp += abs(nowh - newh) + abs(noww - neww)
        S[now + D - 1] = tmp
        now += D

Q = int(input())
for i in range(Q):
    L, R = list(map(int, input().split()))
    ans = S[R - 1] - S[L - 1]
    print(ans)
