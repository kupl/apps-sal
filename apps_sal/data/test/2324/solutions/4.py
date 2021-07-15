s = input()

size = len(s)

dp = [[0 for l in range(size)] for li in range(size)]

ans = [0]*(size+1)

for i in range(1, size+1):
    if i == 1:
        for j in range(0, size):
            dp[j][j] = 1
            ans[1] += 1
    elif i == 2:
        for j in range(0, size-1):
            if s[j+1] == s[j]:
                dp[j][j+1] = 2
                ans[1] += 1
                ans[2] += 1
            else:
                dp[j][j+1] = 0
    else:
        for j in range(0, size-i+1):
            if s[j] != s[j+i-1] or dp[j+1][j+i-2] == 0:
                dp[j][j+i-1] = 0
            else:
                dp[j][j+i-1] = dp[j][int((j+j+i-2)/2)] + 1
                for p in range(1, dp[j][j+i-1]+1):
                    ans[p] += 1

for i in range(1, size):
    print(ans[i], end="")
    print(" ", end="")
print(ans[size])

