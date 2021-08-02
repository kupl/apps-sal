n, a, b, c = map(int, input().split())
if n % 4 == 0:
    print(0)
elif n % 4 == 1:
    print(min(c, a * 3, a + b))
elif n % 4 == 2:
    print(min(c * 2, b, a * 2))
else:  # n % 4 == 3
    print(min(a, b + c, 3 * c))
