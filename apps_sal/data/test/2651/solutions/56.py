(n, m) = map(int, input().split())
xl = list(map(int, input().split()))
yl = list(map(int, input().split()))
xl = list(map(lambda x: x - xl[0], xl))
yl = list(map(lambda x: x - yl[0], yl))
xi = 0
yi = 0
mod = 10 ** 9 + 7
xsum = sum(xl)
ysum = sum(yl)
for i in range(n):
    xi += (xsum - xl[i] * (n - i)) % mod
    xsum -= xl[i]
for j in range(m):
    yi += (ysum - yl[j] * (m - j)) % mod
    ysum -= yl[j]
print(xi * yi % mod)
