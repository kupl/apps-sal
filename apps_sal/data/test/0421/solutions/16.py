def main():
    tt = list(tuple(map(int, input().split())) for _ in range(int(input())))
    tt.sort(key=lambda e: e.__getitem__(1))
    res = t = 0
    for l, r in tt:
        if t < l:
            t = r
            res += 1
    print(res)


def __starting_point():
    main()


__starting_point()
