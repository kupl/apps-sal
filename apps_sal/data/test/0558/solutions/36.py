(n, m, k) = map(int, input().split())
g = 998244353
r = 1
p = pow(m - 1, n - 1, g)
for i in range(1, k + 1):
    r = r * (n - i) * pow(i, g - 2, g) % g
    p = (p + r * pow(m - 1, n - 1 - i, g)) % g
print(m * p % g)
