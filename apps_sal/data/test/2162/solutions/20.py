k = [int(i) for i in input().split(" ")]
n = sum(k)
a = [0] * n
for I in range(3):
    line = [int(i) for i in input().split(" ")]
    for item in line:
        a[item - 1] = I
dp = [1] * n
cur = [-1, -1, -1]
for i in range(n):
    for j in range(a[i] + 1):
        if cur[j] >= 0:
            dp[i] = max(dp[i], 1 + dp[cur[j]])
    cur[a[i]] = i
print(n - max(dp))
