def main():
    input()
    ts = []
    for _ in 0, 1:
        tmp = input().split()
        a, x, l = tmp[0][-1], 0, []
        for st in tmp:
            y = int(st[:-2])
            b = st[-1]
            if a != b:
                l.append(((x, a)))
                x, a = y, b
            else:
                x += y
        l.append(((x, a)))
        ts.append(l)
    t, s = ts
    res, m, x, a, y, b = 0, len(s), *s[0], *s[-1]
    if m == 1:
        res = sum(y - x + 1 for y, b in t if a == b and x <= y)
    elif m == 2:
        i, u = 0, ' '
        for j, v in t:
            if a == u and b == v and x <= i and y <= j:
                res += 1
            i, u = j, v
    else:
        t[:0] = s[1: -1] + [(0, ' ')]
        tmp = [0] * len(t)
        for i, j in zip(list(range(1, len(t))), tmp):
            while j > 0 and t[i] != t[j]:
                j = tmp[j - 1]
            tmp[i] = j + 1 if t[i] == t[j] else j
        m -= 2
        del tmp[-1]
        for i, q in enumerate(tmp):
            if q == m:
                i, u, j, v = *t[i - q], *t[i + 1]
                if a == u and b == v and x <= i and y <= j:
                    res += 1
    print(res)


def __starting_point():
    main()

__starting_point()
