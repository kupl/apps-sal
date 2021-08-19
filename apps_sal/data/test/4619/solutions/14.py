(W, H, N) = list(map(int, input().split()))
X_Y_A = [list(map(int, input().split())) for _ in range(N)]
oX = 0
oY = 0
for (x, y, a) in X_Y_A:
    if a == 1:
        oX = max(x, oX)
    elif a == 2:
        W = min(x, W)
    elif a == 3:
        oY = max(y, oY)
    else:
        H = min(y, H)
print(max(0, W - oX) * max(0, H - oY))
