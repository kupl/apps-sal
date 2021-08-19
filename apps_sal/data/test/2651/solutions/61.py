(n, m) = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = pow(10, 9) + 7
(a, b) = ([0] * (n - 1), [0] * (m - 1))
(c, s) = (n - 1, 0)
for i in range(n - 1):
    s += c
    a[i] = s
    c -= 2
(c, s) = (m - 1, 0)
for i in range(m - 1):
    s += c
    b[i] = s
    c -= 2
(sumx, sumy) = (0, 0)
for i in range(n - 1):
    sumx += a[i] * (x[i + 1] - x[i])
    sumx %= mod
for i in range(m - 1):
    sumy += b[i] * (y[i + 1] - y[i])
    sumy %= mod
ans = sumx * sumy % mod
print(ans)
