M = 998244353
a = range(N := int(input()))
C = M + 1 >> 1
p = [N * C] * N * 3
for i in a:
    p[i + 2] = p[i + 1] + pow(2, 2 * i + 1 - N, M) * (2 * i + 3)
    print(p[min(i, N - 1 - i)] % M)
