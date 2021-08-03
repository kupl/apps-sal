def main():
    input()
    vv = list(map(int, input().split()))
    uu = sorted(vv)
    for tmp in vv, uu:
        a = 0
        for i, b in enumerate(tmp):
            tmp[i] = a
            a += b
        tmp.append(a)
    res = []
    vu = (None, vv, uu)
    for _ in range(int(input())):
        type, l, r = list(map(int, input().split()))
        tmp = vu[type]
        res.append(str(tmp[r] - tmp[l - 1]))
    print('\n'.join(res))


def __starting_point():
    main()


__starting_point()
