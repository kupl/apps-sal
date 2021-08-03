from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    n, q = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))

    dp = [0, float("-inf")]

    for i in range(n):

        ndp = [dp[0], dp[1]]
        ndp[0] = max(ndp[0], dp[1] - a[i])
        ndp[1] = max(ndp[1], dp[0] + a[i])
        dp = ndp

    print(max(dp))
