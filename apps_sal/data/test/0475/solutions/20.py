MOD = 998244353
(n, m, k) = input().split()
n = int(n)
m = int(m)
k = int(k)


def nCr(n, k):
    C = [0 for i in range(k + 1)]
    C[0] = 1
    for i in range(1, n + 1):
        j = min(i, k)
        while j > 0:
            C[j] = C[j] + C[j - 1]
            j -= 1
    return C[k]


answer = m * nCr(n - 1, k) * (m - 1) ** k
print(answer % MOD)
