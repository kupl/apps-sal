for _ in range(int(input())):
    n = int(input())
    res = n
    cur = 0
    for i, c in enumerate(input()):
        if c == '1':
            x = i + 1
            y = n - x + 1
            res = max(res, 2 * x, n + 1, 2 * y)
            cur += 2
        else:
            cur += 1
    print(max(cur, res))
