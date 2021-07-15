import sys
from collections import defaultdict

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    dp = [defaultdict(int) for _ in range(N)]
    for c in 'ACGT':
        dp[0][c + 'XX'] = 1

    for i in range(1, N):
        for s, v in list(dp[i - 1].items()):
            for c in 'AT':
                dp[i][c + s[:2]] = (dp[i][c + s[:2]] + v) % MOD
            if not (s[1] == 'A' and s[0] == 'C'):
                dp[i]['G' + s[:2]] = (dp[i]['G' + s[:2]] + v) % MOD
            if (
                not (s[1] == 'A' and s[0] == 'G')
                and not (s[1] == 'G' and s[0] == 'A')
                and not (s[2] == 'A' and s[1] == 'G')
                and not (s[2] == 'A' and s[0] == 'G')
            ):
                dp[i]['C' + s[:2]] = (dp[i]['C' + s[:2]] + v) % MOD

    ans = sum(dp[N - 1].values()) % MOD
    print(ans)

    return


def __starting_point():
    main()

__starting_point()
