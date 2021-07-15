n = 100001
m = int(input())
div = [[] for _ in range(n)]
div[1] = [1]
for i in range(2, n):
    if not div[i]:
        div[i] = [i]
        for j in range(2 * i, n, i):
            div[j].append(i)
a = list(map(int, input().rstrip().split()))
dp = [0] * (n + 1)
for i in a:
    x = max(dp[j] for j in div[i]) + 1
    for j in div[i]:
        dp[j] = x
print(max(dp))
