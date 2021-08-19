import numpy as np
import sys
sys.setrecursionlimit(10000000)
MOD = 998244353
INF = 10 ** 18


def main():
    (N, S) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    before = np.zeros(S + 1, np.int64)
    before[0] = 1
    ans = 0
    for a in A:
        now = np.zeros(S + 1, np.int64)
        now += before
        now[a:] += before[:-a]
        ans += now[S]
        ans %= MOD
        now[0] += 1
        now = np.mod(now, MOD)
        before = now
    print(ans)


def __starting_point():
    main()


__starting_point()
