import sys
input = sys.stdin.readline


def ot(s):
    return 'A' if s == 'B' else 'B'


mod = 10 ** 9 + 7
N = int(input())
Ss = [input().rstrip() for _ in range(4)]


def solve(caa, cab, cba, cbb):
    if caa == cab or N <= 3:
        return 1
    if cba == 'A':
        dp = [[0, 0] for _ in range(N + 1)]
        dp[0][1] = 1
        for n in range(N):
            dp[n + 1][0] = (dp[n][0] + dp[n][1]) % mod
            dp[n + 1][1] = dp[n][0]
        return dp[N][1]
    else:
        return pow(2, N - 3, mod)


if Ss[1] == 'B':
    Ss = [ot(Ss[3]), 'A', ot(Ss[2]), ot(Ss[0])]
print(solve(Ss[0], Ss[1], Ss[2], Ss[3]))
