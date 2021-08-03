
n, m = list(map(int, input().split()))

M = 1000000007


if m == 1:
    print(n + 1)
else:
    print((m * pow(2 * m - 1, n, M) - pow(m, n, M)) * pow(m - 1, M - 2, M) % M)
