n = int(input())
ar = [int(x) for x in input().split()]
dp = [0] * n
for i in range(n):
    if ar[i] != 0:
        dp[i] += 1
        for j in range(i + 1, n):
            if ar[j] != 0:
                dp[i] += 1
            else:
                break
    if dp[i] >= n - i:
        break
print(max(dp))
