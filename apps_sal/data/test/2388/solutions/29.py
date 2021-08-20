import sys
input = sys.stdin.readline


def solve():
    MOD = 998244353
    N = int(input())
    XDs = [tuple(map(int, input().split())) for _ in range(N)] + [(10 ** 12, 0)]
    XDs.sort()
    Xs = [X for (X, D) in XDs]
    stack = [N]
    dp = [0] * (N + 1)
    dp[-1] = 1
    for i in reversed(list(range(N))):
        (X, D) = XDs[i]
        while Xs[stack[-1]] < X + D:
            stack.pop()
        dp[i] = dp[stack[-1]] + dp[i + 1]
        dp[i] %= MOD
        stack.append(i)
    print(dp[0])


solve()
