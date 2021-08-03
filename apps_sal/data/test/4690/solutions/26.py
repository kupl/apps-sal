a, b, c, d = map(int, input().split())
if a * b - c * d >= 0:
    print(a * b)
else:
    print(c * d)
