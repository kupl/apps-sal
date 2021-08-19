def main():
    n = int(input())
    if n == 1:
        print(-1)
        return
    elif n == 2:
        (a, b) = list(map(int, input().split()))
        res = {a * 2 - b, b * 2 - a}
        if not a + b & 1:
            res.add((a + b) // 2)
    else:
        l = sorted(map(int, input().split()))
        (d, a) = ({}, -l[-1])
        for (i, b) in enumerate(l):
            (x, a) = (b - a, b)
            (cnt, _) = d.get(x, (0, 0))
            d[x] = (cnt + 1, b)
        t = sorted(d.items())
        if len(t) == 2:
            (y, (_, b)) = t[0]
            res = {l[0] - y, b + y}
        elif len(t) == 3:
            ((x, _), (y, (c2, b)), _) = t
            if not x or c2 > 1 or x * 2 != y:
                res = ()
            else:
                res = (b - x,)
        else:
            res = ()
    print(len(res))
    if res:
        print(*sorted(res))


def __starting_point():
    main()


__starting_point()
