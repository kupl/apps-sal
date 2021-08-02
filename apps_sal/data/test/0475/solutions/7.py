import sys

MOD = 998244353

n, m, k = list(map(int, input().strip().split()))

memo = dict()


def C(n, m, k, first):
    if n == 0:
        if k == 0:
            return 1
        else:
            return 0
    if k == 0:
        if first:
            return m
        else:
            return 0

    if (n, m, k, first) in memo:
        return memo[n, m, k, first]

    vseh = 0

    if first:
        for i in range(n):
            vseh += m * C(i, m, k, False)
    else:
        for i in range(n):
            vseh += (m - 1) * C(i, m, k - 1, False)

    memo[n, m, k, first] = vseh % MOD
    return memo[n, m, k, first]


def C2(n, m, k):
    matrika = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    matrika[0][0] = 1
    for j in range(1, k + 1):
        acc = 0
        for a in range(1, n + 1):
            acc += (m - 1) * matrika[j - 1][a - 1]
            matrika[j][a] = acc % MOD

    result = m * sum(matrika[k][:-1])

    return result % MOD


print(C2(n, m, k))
