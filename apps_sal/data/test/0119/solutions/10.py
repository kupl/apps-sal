def main():
    n = int(input())
    seg = []
    for i in range(n):
        (l, r) = map(int, input().split())
        seg.append((l, r, i + 1))
    seg = sorted(seg, key=lambda x: (x[0], -x[1]))
    lar = 0
    sma = -1
    for i in range(1, len(seg)):
        if seg[i][1] <= seg[lar][1]:
            sma = i
            break
        else:
            lar = i
    if sma != -1:
        print(seg[sma][2], seg[lar][2])
    else:
        print(-1, -1)


def __starting_point():
    main()


__starting_point()
