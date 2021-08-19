(a, b, c) = map(int, input().split())
if a - b < c:
    print(c + b - a)
else:
    print(0)
