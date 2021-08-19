for _ in range(int(input())):
    (a, b, c, r) = list(map(int, input().split()))
    if a > b:
        (a, b) = (b, a)
    (x, y) = (c - r, c + r)
    d = max(0, min(b, y) - max(x, a))
    print(b - a - d)
