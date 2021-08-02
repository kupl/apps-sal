M = 998244353
N = int(input())
p = [-~M // 2 * N] * N * 3
for i in range(N):
    p[i + 2] = p[i + 1] + pow(2, 2 * i + 1 - N, M) * (2 * i + 3)
    print(p[min(i, N - 1 - i)] % M)
