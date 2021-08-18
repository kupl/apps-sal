"""
E - Get Everything
https://atcoder.jp/contests/abc142/tasks/abc142_e

"""
import sys


def solve(N, M):
    dp = [float('inf')] * 2**N
    dp[0] = 0
    for y in range(1, M + 1):
        a, b = list(map(int, input().split()))
        c = [int(i) for i in input().split()]
        t = 0
        for cc in c:
            t |= (1 << (cc - 1))
        for x in range(2**N):
            if dp[x | t] > dp[x] + a:
                dp[x | t] = dp[x] + a
    return -1 if dp[-1] == float('inf') else dp[-1]


def main(args):
    N, M = list(map(int, input().split()))
    ans = solve(N, M)
    print(ans)


def __starting_point():
    main(sys.argv[1:])


__starting_point()
