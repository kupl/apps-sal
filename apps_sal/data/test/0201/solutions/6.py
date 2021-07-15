def main():
    c, hr, hb, wr, wb = (int(i) for i in input().split())

    if wb < c**(1/2) > wr:
        if hr / wr < hb / wb:
            wr, hr, wb, hb = wb, hb, wr, hr
        mx = 0
        for i in range(wr + 1):
            tmx = i * hb + ((c - i * wb) // wr) * hr
            mx  = tmx if tmx > mx else mx
    else:
        if wr <= wb:
            wr, hr, wb, hb = wb, hb, wr, hr
        nr = 0
        mx = 0
        while nr * wr <= c:
            tmx = nr * hr + ((c - nr * wr) // wb) * hb
            mx = tmx if tmx > mx else mx
            nr += 1

    print(mx)


def __starting_point():
    main()

__starting_point()
