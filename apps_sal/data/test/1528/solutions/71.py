N, X = map(int, input().split())
L = [[1, 1] for _ in range(N + 1)]
i = 0
while i + 1 <= N:
    L[i + 1][0] = L[i][0] * 2 + 1
    L[i + 1][1] = L[i + 1][0] * 2 - 1
    i += 1

xx = [[1, 1, 1, 1, 1]for _ in range(N + 1)]
i = 0
while i + 1 <= N:
    xx[i + 1][1] = L[i][1] + 1
    xx[i + 1][2] = L[i][1] + 2
    xx[i + 1][3] = 2 * L[i][1] + 2
    xx[i + 1][4] = 2 * L[i][1] + 3
    i += 1

ans = 0
while N > 0:
    if xx[N][0] == X:
        break
    elif xx[N][1] >= X:
        N -= 1
        X -= 1
    elif xx[N][2] == X:
        ans += 1 + L[N - 1][0]
        break
    elif xx[N][3] >= X:
        ans += 1 + L[N - 1][0]
        X -= xx[N][2]
        N -= 1
    else:
        ans += 1 + 2 * L[N - 1][0]
        break
    if N == 0:
        ans += 1

print(ans)
