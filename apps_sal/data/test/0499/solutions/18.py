from collections import namedtuple


def __starting_point():

    n = int(input())
    cards = input()

    r = 0
    g = 0
    b = 0
    for card in cards:
        if card == "R":
            r += 1
        elif card == "G":
            g += 1
        elif card == "B":
            b += 1

    colornum = 0
    if r:
        colornum += 1
    if g:
        colornum += 1
    if b:
        colornum += 1

    res = ""
    if colornum == 3:
        res = "BGR"
    elif colornum == 2:
        if r == 1:
            if b == 1:
                res = "G"
            elif b > 1:
                res = "GR"
            elif g == 1:
                res = "B"
            elif g > 1:
                res = "BR"
        elif g == 1:
            if r == 1:
                res = "B"
            elif b == 1:
                res = "R"
            elif r > 1:
                res = "BG"
            elif b > 1:
                res = "GR"
        elif b == 1:
            if r == 1:
                res = "G"
            elif g == 1:
                res = "R"
            elif r > 1:
                res = "BG"
            elif g > 1:
                res = "BR"
        else:
            res = "BGR"
    else:
        if r:
            res = "R"
        elif g:
            res = "G"
        elif b:
            res = "B"

    print(res)


__starting_point()
