def main():
    import sys
    sys.setrecursionlimit(10 ** 9)
    input = sys.stdin.readline
    mod = 998244353
    N = int(input())
    robot = [tuple(map(int, input().split())) for _ in range(N)]
    robot.sort()
    stack = []
    dp = [1] * (N + 1)
    for i in reversed(range(N)):
        (x, d) = robot[i]
        while stack and robot[stack[-1]][0] < x + d:
            stack.pop()
        if stack:
            dp[i] = dp[i + 1] + dp[stack[-1]]
        else:
            dp[i] = dp[i + 1] + 1
        dp[i] %= mod
        stack.append(i)
    print(dp[0])


main()
