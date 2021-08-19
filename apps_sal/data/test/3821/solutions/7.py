def main():
    input()
    ps = list(map(float, input().split()))
    ps = sorted(ps, reverse=True)
    if ps[0] == 1:
        print(1)
    else:
        p = 1 - ps[0]
        s = ps[0] / (1 - ps[0])
        for x in ps[1:]:
            if s >= 1:
                break
            p *= 1 - x
            s += x / (1 - x)
        print(p * s)


def __starting_point():
    main()


__starting_point()
