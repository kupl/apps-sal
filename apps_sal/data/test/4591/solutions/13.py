(a, b, c, x, y) = map(int, input().split())
A_B = a * x + b * y
AB = 2 * c * max(x, y)
if x == y:
    C = c * 2 * x
elif x > y:
    C = c * 2 * y + a * (x - y)
else:
    C = c * 2 * x + b * (y - x)
print(min(A_B, AB, C))
