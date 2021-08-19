import sys
sys.setrecursionlimit(10 ** 8)


def ni():
    return int(sys.stdin.readline())


def nm():
    return list(map(int, sys.stdin.readline().split()))


def nl():
    return list(nm())


def ns():
    return sys.stdin.readline().rstrip()


MOD = 10 ** 9 + 7
(N, K) = nm()


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


print(solve())
