a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))
if a * d - b * c == 0:
    print(0)
else:
    curpos = a * d - b * c >= 0
    small = 0;
    large = 1e18
    for iteration in range(200):
        avg = (small + large) / 2
        works = False
        for ach in range(-1, 2, 2):
            for bch in range(-1, 2, 2):
                for cch in range(-1, 2, 2):
                    for dch in range(-1, 2, 2):
                        newpos = (a + ach * avg) * (d + dch * avg) - (b + bch * avg) * (c + cch * avg) >= 0
                        if newpos != curpos:
                            works = True
        if works:
            large = avg
        else:
            small = avg
    print(small)
