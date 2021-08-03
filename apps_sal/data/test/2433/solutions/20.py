for _ in range(int(input())):
    b, p, f = list(map(int, input().split()))
    h, c = list(map(int, input().split()))
    res = 0
    b //= 2
    if h > c:
        res += min(p, b) * h
        b -= min(p, b)
        res += min(f, b) * c
    else:
        res += min(f, b) * c
        b -= min(f, b)
        res += min(p, b) * h
    print(res)
