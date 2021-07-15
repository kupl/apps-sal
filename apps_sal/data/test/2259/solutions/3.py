from bisect import bisect_left, bisect_right, insort
R = lambda: map(int, input().split())
n, arr = int(input()), list(R())
dp = []
for i in range(n):
    idx = bisect_left(dp, arr[i])
    if idx >= len(dp):
        dp.append(arr[i])
    else:
        dp[idx] = arr[i]
print(len(dp))
