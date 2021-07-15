for _ in range(int(input())):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    n = b // 2
    res = 0
    for i in range(min(n, p) + 1):
        j = min(n - i, f)
        res = max(res, h * i + c * j)
    print(res)
