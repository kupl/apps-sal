def main():
    n, l, res, a = int(input()), [], [], 0
    aa = list(map(int, input().split()))
    for i, b in enumerate(aa):
        if a >= b:
            l.append(i)
        a = b
    if not l:
        print(n)
        return
    l.append(n)
    rapp, a = res.append, 0
    for b in l:
        rapp(b - a)
        a = b
    a = b = 0
    for c in l:
        if a + 1 < b < c - 1 and (aa[b] - aa[b - 2] > 1 or aa[b + 1] - aa[b - 1] > 1):
            rapp(c - a - 1)
        a, b = b, c
    print(max(res) + 1)


def __starting_point():
    main()


__starting_point()
