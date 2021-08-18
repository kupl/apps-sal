

def f(a):
    n = len(a)
    dp = [0] * n

    s = [0] * (n + 1)

    for i in range(0, n):
        s[i + 1] = s[i] + a[i]

    maxdiffyet = s[n]

    for i in range(n - 2, -1, -1):
        dp[i] = maxdiffyet
        maxdiffyet = max(maxdiffyet, s[i + 1] - dp[i])

    return dp[0]


n = int(input())
a = [int(x) for x in input().split(' ')]

print(f(a))
