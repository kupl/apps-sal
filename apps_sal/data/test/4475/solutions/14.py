for _ in range(int(input())):
    a, b, x, y, n = list(map(int, input().split()))
    c = max(a - n, x)
    d = max(b - n, y)
    if c < d:
        ans = c
        n -= a - c
        d = max(b - n, y)
        print(ans * d)
    else:
        ans = d
        n -= b - d
        c = max(a - n, x)
        print(ans * c)
