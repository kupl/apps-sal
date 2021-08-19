import math


def fillTea(water, cups):
    curW = water
    for i in range(len(cups)):
        curW -= math.ceil(cups[i] / 2)
        cups[i] = [cups[i], i, math.ceil(cups[i] / 2)]
    cups = sorted(cups, key=lambda l: l[0], reverse=True)
    if curW < 0:
        return ['-1']
    curCup = 0
    while curW > 0:
        curP = min(cups[curCup][0] - cups[curCup][2], curW)
        cups[curCup][2] += curP
        curW -= curP
        curCup += 1
    cups = sorted(cups, key=lambda l: l[1], reverse=False)
    for i in range(len(cups)):
        cups[i] = str(cups[i][2])
    if curW < 0:
        return ['-1']
    return cups


'\n3 20\n22 2 1\n'


def __starting_point():
    [n, w] = [int(x) for x in input().split()]
    cups = [int(x) for x in input().split()]
    print(' '.join(fillTea(w, cups)))


__starting_point()
