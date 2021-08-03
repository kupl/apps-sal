def main():
    input()
    ww = list(map(int, input().split()))
    bb = [int(_) - 1 for _ in input().split()]
    aa = []
    for i in bb:
        if i not in aa:
            aa.append(i)
    aa.reverse()
    tot = 0
    for b in bb:
        idx = aa.index(b)
        del aa[idx]
        tot += sum([ww[_] for _ in aa[idx:]])
        aa.append(b)
    print(tot)


def __starting_point():
    main()


__starting_point()
