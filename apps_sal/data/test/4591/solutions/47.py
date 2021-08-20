(a, b, c, x, y) = map(int, input().split())
p = a * x + b * y
q = 2 * c * max(x, y)
r = 2 * c * x + b * (y - x)
s = 2 * c * y + a * (x - y)
if x >= y:
    print(min(p, q, s))
else:
    print(min(p, q, r))
