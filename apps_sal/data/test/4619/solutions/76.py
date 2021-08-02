W, H, N = map(int, input().split())
xya = [list(map(int, input().split())) for i in range(N)]
X = Y = 0
for i in range(N):
    if xya[i][2] == 1:
        X = max(X, xya[i][0])
    if xya[i][2] == 2:
        W = min(W, xya[i][0])
    if xya[i][2] == 3:
        Y = max(Y, xya[i][1])
    if xya[i][2] == 4:
        H = min(H, xya[i][1])
print(max(W - X, 0) * max(H - Y, 0))
