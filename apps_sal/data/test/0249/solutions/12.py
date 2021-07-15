def main():
    from bisect import bisect_left
    n, l, x, y = list(map(int, input().split()))
    aa, d = list(map(int, input().split())), {}
    for z in (x, y, y + x):
        for a in aa:
            a += z
            if a > l:
                break
            b = aa[bisect_left(aa, a)]
            if b <= a:
                if b == a:
                    d[z] = a
                break
        if len(d) == 2:
            break
    if d:
        if x in d and y in d:
            res = []
        elif x in d:
            res = [y]
        elif y in d:
            res = [x]
        elif y + x in d:
            res = [d[y + x] - y]
    else:
        z, tmp = y - x, []
        for a in aa:
            a += z
            if a > l:
                break
            b = aa[bisect_left(aa, a)]
            if b == a:
                tmp.append(a)
        for a in tmp:
            if a > y:
                res = [a - y]
                break
            elif a + x < l:
                res = [a + x]
                break
        else:
            res = [x, y]
    print(len(res))
    if res:
        print(*res)


def __starting_point():
    main()

__starting_point()
