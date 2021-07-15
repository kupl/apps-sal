n, a = list(map(int, input().split()))
x = [int(i)-a for i in input().split()]

dp = {0: 1}

for i in x:
    tmp = list(dp.items())
    for key, value in tmp:
        dp[key+i] = dp.get(key+i, 0) + value
print((dp[0] - 1))



