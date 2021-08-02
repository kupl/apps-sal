a, b, c = map(int, input().split())
a1 = max(a, b, c)
c1 = min(a, b, c)
b1 = a + b + c - a1 - c1

if b1 % 2 == c1 % 2:
    print(int((2 * a1 - c1 - b1) / 2))
else:
    print(int((2 * (a1 + 1) - c1 - b1) / 2) + 1)
