(n, m) = list(map(int, input().split()))
arr = []
for i in range(n):
    l = list(map(float, input().split()))
    arr.append(int(l[0]))
dp = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if arr[j] <= arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
