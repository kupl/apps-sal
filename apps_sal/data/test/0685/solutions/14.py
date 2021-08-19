def main():
    (n, h) = list(map(int, input().split()))
    trans = []
    for i in range(n):
        (a, b) = input().split()
        trans.append((int(a), int(b)))
    lIdx = 0
    rIdx = 0
    mx = -9999999
    height = h
    while rIdx + 1 < n:
        while height > 0 and rIdx + 1 < n:
            rIdx += 1
            height -= trans[rIdx][0] - trans[rIdx - 1][1]
        if height == 0:
            mx = max(mx, trans[rIdx][0] - trans[lIdx][0])
        elif height > 0:
            mx = max(mx, trans[rIdx][1] - trans[lIdx][0] + height)
        else:
            mx = max(mx, trans[rIdx][0] + height - trans[lIdx][0])
        lIdx += 1
        height += trans[lIdx][0] - trans[lIdx - 1][1]
    if height == 0:
        mx = max(mx, trans[rIdx][0] - trans[lIdx][0])
    elif height > 0:
        mx = max(mx, trans[rIdx][1] - trans[lIdx][0] + height)
    else:
        mx = max(mx, trans[rIdx][0] + height - trans[lIdx][0])
    print(mx)


def __starting_point():
    main()


__starting_point()
