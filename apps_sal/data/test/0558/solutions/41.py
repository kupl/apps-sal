(N, M, K) = list(map(int, input().split()))
m = 998244353
result = 0
n = 1
k = 1
for i in range(K + 1):
    result += n * pow(k, m - 2, m) * pow(M - 1, N - 1 - i, m)
    result %= m
    n *= N - 1 - i
    n %= m
    k *= i + 1
    k %= m
result *= M
result %= m
print(result)
