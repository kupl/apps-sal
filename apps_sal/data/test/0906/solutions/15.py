(n, m, k) = map(int, input().split())
a = (n - 1) * (m - 1)
z = 2
if a == 0:
    z = 1
zd = 1
mod = 1000000007
while a > 1:
    if a % 2 == 1:
        zd = zd * z % mod
    z = z * z % mod
    a = a // 2
z = z * zd % mod
if k == -1:
    if n % 2 == m % 2:
        print(z)
    else:
        print(0)
else:
    print(z)
