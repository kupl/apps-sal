mod = 998244353


def pow_(x, p, mod):
    if p == 1:
        return x % mod
    tmp = pow_(x, p // 2, mod)
    if p % 2 == 0:
        return tmp * tmp % mod
    else:
        return tmp * tmp * x % mod


def reverse(x, mod):
    return pow_(x, mod - 2, mod)


n = int(input()) + 1
p = [0] + list(map(int, input().split()))
dp = [0] * n
rev = [0] * 101
for i in range(1, 101):
    rev[i] = reverse(i, mod)
for i in range(1, n):
    dp[i] = (dp[i - 1] + 1) * 100 * rev[p[i]] % mod
print(dp[-1])
