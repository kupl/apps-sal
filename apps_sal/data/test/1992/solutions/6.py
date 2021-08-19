def main():
    (n, m, k) = map(int, input().split())
    aa = [0]
    aainv = [0] * (n + 1)
    for a in map(int, input().split()):
        aainv[a] = len(aa)
        aa.append(a)
    bb = list(map(int, input().split()))
    res = 0
    for b in bb:
        bpos = aainv[b]
        res += (bpos - 1) // k + 1
        if bpos > 1:
            bpos -= 1
            c = aa[bpos]
            aainv[b] = bpos
            aa[bpos] = b
            bpos += 1
            aainv[c] = bpos
            aa[bpos] = c
    print(res)


def __starting_point():
    main()


__starting_point()
