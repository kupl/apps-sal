import math
dp = [[[math.inf for i in range(105)] for i in range(105)] for i in range(105)]

n, m, k = list(map(int, input().split()))
k += 1

z = list(map(int, input().split()))
matrix = []
for i in range(n):
    ans = list(map(int, input().split()))
    matrix.append(ans)
for i in range(len(z)):
    if(i == 0):
        if(z[i] != 0):
            dp[0][1][z[i] - 1] = 0
        else:
            for x in range(m):
                dp[0][1][x] = matrix[i][x]
    else:
        if(z[i] != 0):
            col = z[i] - 1
            if(z[i - 1] != 0):
                col2 = z[i - 1] - 1
                if(col2 == col):
                    for j in range(k):
                        if(j == 0):
                            continue
                        dp[i][j][col] = min(dp[i - 1][j][col], dp[i][j][col])

                else:
                    for j in range(k):
                        if(j == 0):
                            continue
                        dp[i][j][col] = min(dp[i - 1][j - 1][col2], dp[i][j][col])

            else:
                pq = []
                for t in range(k):
                    if(t == 0):
                        continue
                    pq = []
                    for x in range(m):
                        pq.append([dp[i - 1][t - 1][x], x])
                    pq.append([math.inf, math.inf])
                    pq.sort()
                    col = z[i] - 1
                    if(col != pq[0][1] and pq[0][0] != math.inf):
                        dp[i][t][col] = min(dp[i][t][col], pq[0][0], dp[i - 1][t][col])
                    elif(pq[0][0] != math.inf and col == pq[0][1]):
                        dp[i][t][col] = min(dp[i][t][col], pq[1][0], dp[i - 1][t][col])
                    elif(pq[0][0] == math.inf):
                        dp[i][t][col] = min(dp[i][t][col], dp[i - 1][t][col])

        else:
            if(z[i - 1] != 0):
                col = z[i - 1] - 1
                for t in range(k):
                    if(t == 0):
                        continue
                    for x in range(m):
                        if(x != col):
                            dp[i][t][x] = min(dp[i][t][x], dp[i - 1][t - 1][col] + matrix[i][x])
                        else:
                            dp[i][t][x] = min(dp[i][t][x], dp[i - 1][t][col] + matrix[i][x])

            else:
                for t in range(k):
                    if(t == 0):
                        continue
                    pq = []
                    for x in range(m):
                        pq.append([dp[i - 1][t - 1][x], x])
                    pq.append([math.inf, math.inf])
                    pq.sort()

                    for v in range(m):
                        if(v != pq[0][1]):
                            dp[i][t][v] = min(dp[i][t][v], pq[0][0] + matrix[i][v], dp[i - 1][t][v] + matrix[i][v])
                        else:
                            dp[i][t][v] = min(dp[i][t][x], dp[i - 1][t][v] + matrix[i][v], pq[1][0] + matrix[i][v])


mini = math.inf


for i in range(m):
    mini = min(mini, dp[n - 1][k - 1][i])
if(mini == math.inf):
    print(-1)
else:
    print(mini)
