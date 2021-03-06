def __starting_point():
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    mindiff = float('inf')
    for (i, num) in enumerate(a):
        diff = (b[-1] - num) % m
        _a = [(i + diff) % m for i in a]
        _a.sort()
        if _a == b:
            mindiff = min(mindiff, diff)
    print(mindiff)


__starting_point()
