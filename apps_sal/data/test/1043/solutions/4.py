from sys import stdin

input = stdin.readline

n = int(input())

a = list(map(int, input().split()))
a.reverse()

inf = float('inf')
N = 19
dp = [[inf] * (N+2) for _ in range(1 << N)]

sum = [0] * (1 << 21)
now = n
for i in range(1, 20):
    sum[i] = sum[i-1] + now // 2
    now //= 2


for i in range(n)[::-1]:
    for j in range(N):
        if a[i] == -1:
            dp[i][j] = 0
            continue

        if i > sum[j]:
            continue
        dp[i][j] = dp[i + 1][j + 1] + a[i]
        if i < sum[j]:
            dp[i][j] = min(dp[i][j], dp[i + 1][j])
        # print(i, j, dp[i][j])

print(dp[0][0])
