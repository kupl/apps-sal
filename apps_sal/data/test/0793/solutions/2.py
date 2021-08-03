MOD = 10 ** 9 + 7
n, m = list(map(int, input().split()))
s = list(map(int, input().split()))
t = list(map(int, input().split()))

dp = [0] * n
for tj in t:
    acc = 0
    for i, si in enumerate(s):
        acc = (acc + dp[i]) % 1000000007
        if si == tj:
            dp[i] = (acc + 1) % 1000000007
ans = 1
for x in dp:
    ans = (ans + x) % MOD
print(ans)
