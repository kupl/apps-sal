for _ in range(int(input())):
    (a, b, c, r) = map(int, input().split())
    (a, b) = (min(a, b), max(a, b))
    n = b - a
    (l, f) = (c - r, c + r)
    if a > l:
        (a, b, l, f) = (l, f, a, b)
    if l >= b:
        print(n)
    elif f <= b:
        print(n - (f - l))
    else:
        print(n - (b - l))
