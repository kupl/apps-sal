for i in range(int(input())):
    a, b, c, r = map(int, input().split())
    x = c - r
    y = c + r
    if a > b:
        a, b = b, a
    z = max(0, min(y, b) - max(x, a))
    print(b - a - z)
