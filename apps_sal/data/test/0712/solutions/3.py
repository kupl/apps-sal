a, b, c = list(map(float, input().split(' ')))
a = int(a)
c = int(c)
#dp[i][j] = probability that after i seconds, ther are j ppl on escalator
dp = [[0] * (c+1) for _ in range(c+1)]

for i in range(c+1):
    for j in range(c+1):
        if i == 0:
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = 0
        else:
            if j > a:
                dp[i][j] = 0
            elif j == a:
                dp[i][j] = dp[i-1][j-1]*b + dp[i-1][j]                
            else:
                dp[i][j] = (1-b) * dp[i-1][j] + b * dp[i-1][j-1]
sumx = 0
for i in range(c+1):
    sumx += i * dp[c][i]
print(sumx)

