def main():
    n = int(input())
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    ai = sorted(range(len(aa)), key=aa.__getitem__)
    bi = sorted(range(len(bb)), key=bb.__getitem__)
    res = []
    for a, b in zip(ai, bi):
        if aa[a] != bb[b]:
            break
    else:
        a = ai[-1]
    res.append(aa[a])
    del aa
    del ai
    cc = list(map(int, input().split()))
    ci = sorted(range(len(cc)), key=cc.__getitem__)
    for b, a in zip(bi, ci):
        if bb[b] != cc[a]:
            break
    else:
        b = bi[-1]
    res.append(bb[b])

    print('\n'.join(map(str, res)))


def __starting_point():
    main()
__starting_point()
