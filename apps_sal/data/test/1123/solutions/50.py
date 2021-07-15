import sys

sys.setrecursionlimit(10 ** 8)
ni = lambda: int(sys.stdin.readline())
nm = lambda: list(map(int, sys.stdin.readline().split()))
nl = lambda: list(nm())
ns = lambda: sys.stdin.readline().rstrip()

MOD = 10 ** 9 + 7
N, K = nm()


def solve():
    ans = 0
    tbl = [0] * (K + 1)
    for i in range(K, 0, -1):
        m = K // i
        p = pow(m, N, MOD)

        j = 2
        while j * i <= K:
            p += MOD - tbl[j * i] % MOD
            p %= MOD
            j += 1
        tbl[i] = p

        ans += i * p % MOD
        ans %= MOD
    return ans


print((solve()))

