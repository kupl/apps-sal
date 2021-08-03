from sys import stdin
input = stdin.readline
n, m = list(map(int, input().split()))
arr = list(list(map(int, input().split())) for _ in range(n))
dp = [[1 for i in range(m)] for j in range(n)]

for i in range(1, n):
    for j in range(m):
        if arr[i][j] >= arr[i - 1][j]:
            dp[i][j] = dp[i - 1][j] + 1

dp, all_res = [max(i) for i in dp], []
k = int(input())
quries = list(list(map(int, input().split())) for _ in range(k))
for l, r in quries:
    all_res.append('Yes' if dp[r - 1] >= r - l + 1 else 'No')
print('\n'.join(all_res))
