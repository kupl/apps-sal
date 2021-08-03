t = int(input())

for _ in range(0, t):

    a = list(input())
    nowx = 0
    nowy = 0
    maxx = 0
    minx = 0
    maxy = 0
    miny = 0
    tmaxx = 0
    tminx = 0
    tmaxy = 0
    tminy = 0
    highw = 0
    highs = 0
    widthd = 0
    widtha = 0
    for i in range(0, len(a)):

        if a[i] == 'W':
            nowy += 1
            if nowy >= maxy:
                maxy = nowy
                tmaxy = i

        elif a[i] == 'S':
            nowy -= 1
            if nowy <= miny:
                miny = nowy
                tminy = i
        elif a[i] == 'D':
            nowx += 1
            if nowx >= maxx:
                maxx = nowx
                tmaxx = i
        elif a[i] == 'A':
            nowx -= 1
            if nowx <= minx:
                minx = nowx
                tminx = i

        highw = max(highw, nowy - miny)
        highs = max(highs, maxy - nowy)
        widthd = max(widthd, nowx - minx)
        widtha = max(widtha, maxx - nowx)
    y1 = max(highw, highs)
    y2 = max(highw != 0 or highs != 0, y1 - ((highw != highs)))
    x1 = max(widthd, widtha)
    x2 = max(widthd != 0 or widtha != 0, x1 - ((widthd != widtha)))
    print(min((y1 + 1) * (x2 + 1), (1 + y2) * (x1 + 1)))
