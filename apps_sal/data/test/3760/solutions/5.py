import math
n, m, x, y, a, b = map(int, input().split())
gcd = math.gcd(a, b)
a //= gcd
b //= gcd
max_ratio = min(n // a, m // b)
a *= max_ratio
b *= max_ratio
x1 = max(0, min(x - (a + 1) // 2, n - a))
y1 = max(0, min(y - (b + 1) // 2, m - b))
print(x1, y1, x1 + a, y1 + b)
