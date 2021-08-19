mod = 10**9 + 7
l = input()
bit = [int(i) for i in l]
m = len(bit)
# num1=sum(bit)
# print(bit)
# print(m)
# print(num1)
# ans=0
# ans+=(pow(3,m-1,mod))
# 最上位bitの時
# ans+=(2*pow(2,num1-1,mod))
# print(ans%mod)

# 適当にやりすぎたけど、桁DPジャン
# 小さい方と同じ方
dp = [[0, 0] for i in range(m)]
dp[0] = [1, 2]
for i in range(m - 1):
    dp[i + 1][0] = 3 * dp[i][0] % mod
    if bit[i + 1] == 0:
        dp[i + 1][1] += dp[i][1]
        dp[i + 1][1] %= mod
    else:
        dp[i + 1][0] += dp[i][1]
        dp[i + 1][1] += (2 * dp[i][1])
        dp[i + 1][0] %= mod
        dp[i + 1][1] %= mod
print(sum(dp[m - 1]) % mod)
