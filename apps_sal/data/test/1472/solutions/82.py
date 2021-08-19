from collections import Counter


def main():
    (n, x, y) = map(int, input().split())
    (x, y) = (x - 1, y - 1)
    ans = []
    for i in range(n):
        dp = [n] * n
        dp[i] = 0
        calcstep(i, dp)
        dp[y] = min(dp[y], dp[x] + 1)
        dp[x] = min(dp[x], dp[y] + 1)
        calcstep(x, dp)
        calcstep(y, dp)
        ans += dp
    ans = Counter(ans)
    for i in range(1, n):
        print(ans[i] // 2)


def calcstep(i, dp):
    for j in range(i, len(dp) - 1):
        if dp[j + 1] > dp[j] + 1:
            dp[j + 1] = dp[j] + 1
        else:
            break
    for j in range(1, i + 1)[::-1]:
        if dp[j - 1] > dp[j] + 1:
            dp[j - 1] = dp[j] + 1
        else:
            break


def __starting_point():
    main()


__starting_point()
