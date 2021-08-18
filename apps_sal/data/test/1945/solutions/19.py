def input_split(f): return list(map(f, input().split()))


def main():
    n = int(input())
    vals = []
    for i in range(n):
        vals.append(tuple(input_split(str)))

    res = {}
    for o, n in vals:
        if o in res:
            res[n] = res[o]
            del res[o]
        else:
            res[n] = o
    print(len(res))
    for k in res:
        print("{} {}".format(res[k], k))


def __starting_point():
    main()


__starting_point()
