from sys import stdin

input = stdin.readline
r = list(map(int, input().split()))
n = sum(r)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

mp = [0] * -~n
for i in a:
    mp[i] = 0

for i in b:
    mp[i] = 1

for i in c:
    mp[i] = 2
inf = float('inf')
dp = [[inf] * -~n for _ in range(3)]

for i in range(3):
    dp[i][0] = 0
    for j in range(1, n + 1):
        dp[i][j] = dp[i][j - 1] + (mp[j] != i)
        if i:
            dp[i][j] = min(dp[i - 1][j], dp[i][j])

print(dp[2][n])
