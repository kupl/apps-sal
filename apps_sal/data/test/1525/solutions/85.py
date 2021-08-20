(h, w, k) = list(map(int, input().split()))
p = 10 ** 9 + 7
DP = [[0 for j in range(w + 1)] for i in range(h + 1)]
DP[0][0] = 1
F = [1, 1, 2, 3, 5, 8, 13, 21]
for i in range(h):
    for j in range(w):
        a = DP[i][j - 1] * F[j - 1] * F[w - 1 - j]
        b = DP[i][j] * F[j] * F[w - 1 - j]
        c = DP[i][j + 1] * F[j] * F[w - 2 - j]
        DP[i + 1][j] = (a + b + c) % p
print(DP[h][k - 1])
