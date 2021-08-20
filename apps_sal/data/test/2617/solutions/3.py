t = int(input())
for _ in range(t):
    w = int(input())
    res = []
    for i in range(300):
        if 2 ** (i + 1) - 1 > w:
            break
        res.append((2 ** i, 2 ** (i + 1) - 1))
    (last_n, last_w) = res[-1]
    if last_w != w:
        if last_w + last_n <= w:
            res.append((w - last_w, w))
        else:
            res = res[:-1]
            (last_n, last_w) = res[-1]
            necc = w - last_w - 2 * last_n
            ok = False
            n = last_n
            for x in range(min(necc // 2 + 1, n // 3 + 5), -1, -1):
                y = necc - 2 * x
                if 0 <= x and x <= n and (0 <= y) and (y <= n + x):
                    ok = True
                    res.append((last_n + x, last_w + last_n + x))
                    res.append((last_n + x + y, last_w + 2 * last_n + 2 * x + y))
                    break
            if not ok:
                exit(228)
    print(len(res) - 1)
    for i in range(len(res) - 1):
        print(res[i + 1][0] - res[i][0], end=' ')
    print()
