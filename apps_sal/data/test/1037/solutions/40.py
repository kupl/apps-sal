n = int(input())
a = list(map(int, input().split()))
assert len(a) == n

# 添字のリスト
p = list(range(n))
p.sort(key=lambda i: a[i])

# dp[j] = 位置jから幅iの区間に小さい方からi個を配置したときの最大うれしさ
dp = [0] * (n + 1)

for i in range(n):
    for j in range(n - i):
        dp[j] = max(dp[j] + a[p[i]] * abs(p[i] - (j + i)),
                    dp[j + 1] + a[p[i]] * abs(p[i] - j))

print(dp[0])
