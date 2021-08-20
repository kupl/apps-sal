(N, K) = map(int, input().split())
cnt = 0
for X in range(2, 2 * N + 1):
    Y = X - K
    if 2 <= Y <= 2 * N:
        if X <= N + 1:
            cx = X - 1
        else:
            cx = 2 * N + 1 - X
        if Y <= N + 1:
            cy = Y - 1
        else:
            cy = 2 * N + 1 - Y
        cnt += cx * cy
print(cnt)
