def main():
    n, m = map(int, input().split())
    qry = [list(map(int, input().split())) for _ in range(m)]
    ans = -1
    for v in range(0, 1000):
        s = str(v)
        if len(s) != n:
            continue
        f = True
        for p, x in qry:
            if s[p - 1] != str(x):
                f = False
                break
        if f:
            ans = v
            break
    print(ans)


def __starting_point():
    main()


__starting_point()
