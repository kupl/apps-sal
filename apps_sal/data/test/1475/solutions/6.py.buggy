
n, b, k, x = map(int, input().split())
arr = list(map(int, input().split()))

flg = [0] * x
mod = 10**9 + 7

for i in arr:
    flg[i % x] += 1


def mul(dp, flg, rank):
    nonlocal x
    res = [0] * x
    for i in range(x):
        for j in range(x):
            res[((i * rank) % x + j) % x] += dp[i] * flg[j] % mod
            res[((i * rank) % x + j) % x] %= mod
            # print(i,j,dp[i],dp[j],res[ ( (i*rank)%x+j)%x ])
    return res


def pow(n):
    nonlocal x
    res = 1
    base = 10
    while n:
        if n & 1:
            res = (res * base) % x
        base = (base * base) % x
        n >>= 1
    return res


dp = [0] * x
dp[0] = 1
# print(mul(dp,flg,1))
rank = 1
while b:
    if b & 1:
        dp = mul(dp, flg, pow(rank))
    flg = mul(flg, flg, pow(rank))
    rank <<= 1
    b >>= 1

print(dp[k])
