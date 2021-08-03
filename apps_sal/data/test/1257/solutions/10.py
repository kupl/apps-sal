N, k = map(int, input().split())
a = [[0] * (N + 1) for i in range(N + 1)]
x = N * (k - 1) + 1
S = 0
for i in range(1, N + 1):
    S += x
    a[i][k] = x
    x += 1
    for j in range(k + 1, N + 1):
        a[i][j] = x
        x += 1
x = 1
for i in range(1, N + 1):
    for j in range(1, k):
        a[i][j] = x
        x += 1
print(S)
for i in range(1, N + 1):
    print(*a[i][1:])
