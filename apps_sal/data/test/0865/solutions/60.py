import numpy as np

N, T = list(map(int, input().split()))
T -= 1

AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key = lambda x: x[1])
AB.sort(key = lambda x: x[0], reverse = True)

dp = [[0] * (T + 1) for _ in range(N + 1)]

dp = np.zeros(T + 1, dtype = np.int32)

ans = AB[N - 1][1]
for i in range(N - 1, 0, -1):
    # for j in range(T + 1):
    #     if j < AB[i][0]:
    #         dp[i][j] = dp[i + 1][j]
    #     else:
    #         dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - AB[i][0]] + AB[i][1])
    if AB[i][0] <= T + 1:
        dp[AB[i][0]:] = np.maximum(dp[AB[i][0]:], dp[:T + 1 - AB[i][0]] + AB[i][1])
    tmp = dp[T] + AB[i - 1][1]
    ans = max(ans, tmp)
    
print (ans)
# print (AB)

# for i in dp:
#     print (dp)

