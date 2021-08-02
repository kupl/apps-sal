def main():
    xlat = list(map(int, input().split()))
    dd = [{} for _ in range(26)]
    m = res = 0
    s = input()
    for c in s:
        cx = ord(c) - 97
        d = dd[cx]
        res += d.get(m, 0)
        m += xlat[cx]
        d[m] = d.get(m, 0) + 1
    print(res)


def __starting_point():
    main()


__starting_point()
