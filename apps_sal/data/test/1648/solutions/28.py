import sys
sys.setrecursionlimit(3000)
N, K = map(int, input().split())


def comb(n, k):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if k < 0:
        return 0
    if k == 0:
        return 1
    return comb(n - 1, k - 1) * n // k


R = N - K
MOD = 10**9 + 7
A = K - 1
B = R - 1
if N == K:
    print(1)
    for i in range(2, K + 1):
        print(0)
else:
    for i in range(1, K + 1):
        x = comb(A, i - 1)
        y = comb(B, i - 2)
        z = comb(B, i - 1)
        w = comb(B, i)
        ans = x * (y + 2 * z + w)
        print(ans % MOD)
