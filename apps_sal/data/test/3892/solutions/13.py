def prog():
    n, m = map(int, input().split())
    d = {i: [] for i in range(1, n + 1)}
    from sys import stdin
    for i in range(m):
        a, b = map(int, stdin.readline().split())
        d[a].append(b)
    res = []
    for i in range(1, n + 1):
        lst = []
        for j, x in enumerate(d):
            mn, k = 100000, -1
            for k, y in enumerate(d[x]):
                if x < y:
                    a = y - x
                else:
                    a = n - x + y
                if a < mn:
                    mn = a
            if k > -1:
                if i <= x:
                    b = x - i
                else:
                    b = n - i + x
                lst.append(k * n + mn + b)
        res.append(max(lst))
    print(*res)


prog()
