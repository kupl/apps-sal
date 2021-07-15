for TT in range(1, int(input()) + 1):
    a, b, c = map(int, input().split())
    res = 0
    for x in range(min(a, b // 2) + 1):
        y = min(b - 2 * x, c // 2)
        res = max(res, 3 * (x + y))
    print(res)
