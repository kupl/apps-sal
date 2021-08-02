a, b, c, x, y = map(int, input().split())

if a >= 2 * c and b >= 2 * c:
    print(max(x, y) * 2 * c)
elif a >= 2 * c:
    print(x * 2 * c + max(0, (y - x) * b))
elif b >= 2 * c:
    print(y * 2 * c + max(0, (x - y) * a))
elif a + b > 2 * c and x < y:
    print(x * 2 * c + (y - x) * b)
elif a + b > 2 * c:
    print(y * 2 * c + (x - y) * a)
else:
    print(x * a + y * b)
