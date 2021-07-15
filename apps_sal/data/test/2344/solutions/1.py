n = int(input())
if n == 0:
    print('0')
else:
    data = []
    ans = 0
    for i in range(n):
        line = list(map(lambda entry: int(entry), input().split()))
        x = line[0]-line[1]*line[2]
        if x > 0:
            ans += x
            line[0] -= x
        data.append((line[0], line[1]))
    data.sort(key = lambda entry: -entry[1])
    dp = [[0 for i in range(n)]]
    for j in range(n):
        x = data[j][0]
        nextline = [max(x, dp[-1][0])]
        for i in range(1, n):
            x -= data[j][1]
            nextline.append(max(x + dp[-1][i - 1], nextline[-1], dp[-1][i]))
        dp.append(nextline)
    ans += dp[n][n-1]
    print(ans)
