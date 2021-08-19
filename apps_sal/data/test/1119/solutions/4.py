mod = 1000000007
N = 1005
# input start
k, pa, pb = list(map(int, input().split()))
dp = [[0 for x in range(k)] for y in range(k + 1)]
# end of input


def fast_expo(a, b):
    ret = 1
    while b:
        if b % 2 == 1:
            ret = ret * a % mod
        b //= 2
        a = a * a % mod
    return ret


def inv(x):
    return fast_expo(x, mod - 2) % mod


def dp_val(a, b):
    if b >= k:
        return b
    return dp[a][b]


for i in range(k):
    dp[k][i] = (i + k + pa * inv(pb)) % mod

den = inv(pa + pb)

for i in range(k - 1, 0, -1):
    for j in range(k - 1, -1, -1):
        dp[i][j] = pa * dp_val(i + 1, j) * den % mod + pb * dp_val(i, i + j) * den % mod
        dp[i][j] %= mod

print(dp[1][0])
