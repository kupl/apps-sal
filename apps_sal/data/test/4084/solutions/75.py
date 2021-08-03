n, a, b = map(int, input().split())
x, y = divmod(n, a + b)
if y > a:
    y = a
print((x * a) + y)
