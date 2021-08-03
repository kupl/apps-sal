from fractions import gcd

n, m, x, y, a, b = list(map(int, input().split()))
g = gcd(a, b)
a, b = a // g, b // g
k = min(n // a, m // b)
a, b = k * a, k * b

x1, x2 = x - (a - a // 2), x + a // 2
y1, y2 = y - (b - b // 2), y + b // 2
d = max(0, 0 - x1)
x1, x2 = x1 + d, x2 + d
d = max(0, x2 - n)
x1, x2 = x1 - d, x2 - d
d = max(0, 0 - y1)
y1, y2 = y1 + d, y2 + d
d = max(0, y2 - m)
y1, y2 = y1 - d, y2 - d
print((" ".join(map(str, [x1, y1, x2, y2]))))
