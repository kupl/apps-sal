from fractions import gcd
n, m, x, y, a, b = list(map(int, input().split()))
k = gcd(a, b)
a //= k
b //= k
times = min(n // a, m // b)
a *= times
b *= times
x1 = x - (a + 1) // 2
y1 = y - (b + 1) // 2
if x1 < 0:
    x1 = 0
if y1 < 0:
    y1 = 0
if x1 + a > n:
    x1 -= (x1 + a - n)
if y1 + b > m:
    y1 -= (y1 + b - m)
print(x1, y1, x1 + a, y1 + b)

