def add(a, b):
    a = a % (1000000000 + 7)
    b = b % (1000000000 + 7)
    return (a + b) % (1000000000 + 7)


n = int(input())
i = 1
statements = []
dp = [[0 for i in range(n)] for i in range(n)]
prefix = [[0 for i in range(n)] for i in range(n)]
while(i <= n):
    s = input()
    statements.append(s)
    i += 1

dp[0][0] = 1
prefix[0][0] = 1
j = 1
while(j < n):
    dp[0][j] = 0
    prefix[0][j] = dp[0][j] + prefix[0][j - 1]
    j += 1

i = 1
while(i < n):
    if(statements[i - 1] == 'f'):
        j = 1
        while(j < n):
            dp[i][0] = 0
            prefix[i][0] = 0
            dp[i][j] = dp[i - 1][j - 1]
            prefix[i][j] = add(prefix[i][j - 1], dp[i][j])

            j += 1
    else:
        j = 0
        while(j < n):
            if(j == 0):
                dp[i][j] = prefix[i - 1][n - 1]
            else:
                dp[i][j] = prefix[i - 1][n - 1] - prefix[i - 1][j - 1]
            prefix[i][j] = add(prefix[i][j - 1], dp[i][j])
            j += 1
    # print(prefix)
    i += 1

# i=0
# while(i<n):
# 	j=0
# 	while(j<n):
# 		print(dp[i][j])
# 		j+=1
# 	i+=1

# print(dp)

ans = 0
j = 0
while(j < n):
    ans = add(ans, dp[n - 1][j])
    j += 1

print(ans % (1000000000 + 7))
