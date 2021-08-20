def main():
    n = int(input())
    l = sorted(map(int, input().split()))
    if n == 1:
        print(-1)
        return
    elif n == 2:
        (a, b) = l
        res = {a * 2 - b, b * 2 - a}
        if not a + b & 1:
            res.add((a + b) // 2)
    else:
        q = min(l[1] - l[0], l[-1] - l[-2])
        (a, res) = (l[0] - q, ())
        for b in l:
            if q != b - a:
                if res or q * 2 != b - a:
                    res = ()
                    break
                else:
                    res = (b - q,)
            a = b
        else:
            if not res:
                res = {l[0] - q, b + q}
    print(len(res))
    if res:
        print(*sorted(res))


def __starting_point():
    main()


__starting_point()
