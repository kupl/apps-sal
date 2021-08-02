from math import ceil
mod = 10 ** 9 + 7


def f(l, r, x):
    return ceil((r - x) / 3) - ceil((l - 1 - x) / 3)


n, l, r = map(int, input().split())
m1 = f(l, r, 0)
m2 = f(l, r, 1)
m0 = f(l, r, 2)
dp0 = [1 for i in range(n + 1)]
dp1 = [0 for i in range(n + 1)]
dp2 = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    dp0[i] = (dp0[i - 1] * m0 + dp1[i - 1] * m2 + dp2[i - 1] * m1) % mod
    dp1[i] = (dp1[i - 1] * m0 + dp2[i - 1] * m2 + dp0[i - 1] * m1) % mod
    dp2[i] = (dp2[i - 1] * m0 + dp0[i - 1] * m2 + dp1[i - 1] * m1) % mod
print(dp0[n])
