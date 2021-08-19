n = int(input())


a = list(map(int, input().split()))

dp = [0, ]

count = [0 for i in range(n)]

count[0] += 1

for i in range(n - 1):

    dp.append(dp[a[i] - 1] + 1)

    count[dp[-1]] += 1

ans = 0

for i in range(n):

    ans += count[i] % 2

print(ans)


# Made By Mostafa_Khaled
