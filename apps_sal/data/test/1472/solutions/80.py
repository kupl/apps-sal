N, X, Y = map(int, input().split())
k = [0] * (N - 1)

for i in range(1, N):
    for j in range(i + 1, N + 1):
        tmp = min(abs(i - j), abs(X - i) + 1 + abs(j - Y))
        k[tmp - 1] += 1

for ans in k:
    print(ans)
