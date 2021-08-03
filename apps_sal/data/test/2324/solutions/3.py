s = input().strip()
n = len(s)
pl = [0] * (n + 1)

dp = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n - i):
        l = j + i
        if i == 0:
            dp[j][l] = 1
            pl[1] += 1
        elif i == 1:
            if s[j] == s[l]:
                dp[j][l] = 2
                pl[2] += 1
        else:
            if s[j] == s[l] and dp[j + 1][l - 1] > 0:
                if (i + 1) % 2 == 0:
                    mid = int((i + 1) / 2) - 1
                    dp[j][l] = dp[j][j + mid] + 1
                    pl[dp[j][l]] += 1
                else:
                    mid = int((i + 1) / 2) - 1
                    dp[j][l] = dp[j][j + mid] + 1
                    pl[dp[j][l]] += 1

ans = ''
for i in range(n - 1, -1, -1):
    pl[i] += pl[i + 1]
for i in range(1, n + 1):
    ans = ans + str(pl[i]) + ' '
print(ans)
