n = int(input())
a = list(map(int, input().split()))
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


def create_gt(gt):
    for i in range(2, len(gt)):
        gt[i] = gt[i - 1] * i % mod


def kCn(k, n, mod):
    return gt[n] * reverse(gt[k], mod) * reverse(gt[n - k], mod) % mod


def create_kcn(N, mod):
    kcn = [[0] * N for _ in range(N)]
    kcn[0][0] = 1
    for n in range(1, N):
        for k in range(n, -1, -1):
            kcn[k][n] = (kcn[k - 1][n - 1] + kcn[k][n - 1]) % mod
    return kcn


kcn = create_kcn(1001, mod)
dp = [-1] * n
for i in range(n - 2, -1, -1):
    if a[i] > 0 and i + a[i] < n:
        temp = 0
        for j in range(i + a[i] + 1, n):
            if dp[j] > 0:
                temp = (temp + dp[j] * kcn[a[i]][j - i - 1]) % mod
        temp = (temp + kcn[a[i]][n - i - 1]) % mod
        dp[i] = temp
print(sum([x for x in dp if x > 0]) % mod)
