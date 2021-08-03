a, b, c, x, y = map(int, input().split())
n = a * x + b * y
m = 2 * c * max(x, y)

p = b if x < y else a
l = 2 * c * min(x, y) + p * abs(x - y)

ans = min(n, min(m, l))
print(ans)
