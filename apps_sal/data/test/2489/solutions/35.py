n = int(input())
a = list(map(int, input().split()))
a.sort()
am = max(a)
dp = [[True, 0] for _ in range(am + 1)]
count = 0
for i in a:
    if dp[i][0] == False:
        continue
    else:
        if dp[i][1] == 1:
            dp[i][0] = False
            count -= 1
        else:
            dp[i][1] = 1
            count += 1
            for j in range(2 * i, am + 1, i):
                dp[j][0] = False
print(count)
