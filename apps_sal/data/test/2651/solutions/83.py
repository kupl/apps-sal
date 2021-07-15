n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10 ** 9 + 7

xsm = 0
for i, ex in enumerate(x, 1):
    xsm -= ex * (n - i)
    xsm += ex * (i - 1)
    xsm %= mod

ysm = 0
for i, ey in enumerate(y, 1):
    ysm -= ey * (m - i)
    ysm += ey * (i - 1)
    ysm %= mod

ans = xsm * ysm % mod
print(ans)

