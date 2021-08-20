def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ss = []
        for i in range(n):
            (l, r) = [int(x) for x in input().split()]
            ss.append((l, i, r))
        ttt = []
        cc = 0
        for t in ss:
            if t[0] >= cc:
                ttt.append(t[0])
                cc = t[0] + 1
            elif cc > t[2]:
                ttt.append(0)
            else:
                ttt.append(cc)
                cc += 1
        print(' '.join((str(x) for x in ttt)))


def __starting_point():
    main()


__starting_point()
