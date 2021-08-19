gans = []
for _ in range(int(input())):
    (a, b) = map(int, input().split())
    w = list(map(int, list(input())))
    u = []
    k = 1
    for i in range(1, len(w)):
        if w[i] == w[i - 1]:
            k += 1
        else:
            u.append([w[i - 1], k])
            k = 1
    u.append([w[-1], k])
    dp = [0] * len(u)
    if u[0][0] == 1:
        dp[0] = a
    for i in range(1, len(u)):
        if u[i][0] == 0:
            dp[i] = dp[i - 1]
        elif i == 1:
            dp[i] = dp[i - 1] + a
        else:
            dp[i] = min(dp[i - 1] + a, dp[i - 1] + b * u[i - 1][1])
    gans.append(dp[-1])
print(*gans, sep='\n')
