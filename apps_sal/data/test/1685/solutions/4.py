from math import log
n, q = [int(i) for i in input().split()]
maxlvl = int(log(n + 1, 2)) + 1
steps = [2 ** i for i in range(maxlvl)]


def calc_lvl(m):
    for lvl in range(1, maxlvl):
        if (m - steps[lvl - 1]) % steps[lvl] == 0:
            return (lvl, ((m - steps[lvl - 1]) % (2 * steps[lvl]) == 0))


for i in range(q):
    strt = int(input())
    qwery = input()
    lvl, ind = calc_lvl(strt)

    for c in qwery:
        if c == 'U':
            if strt == steps[-2]:
                continue
            if not ind:
                strt -= steps[lvl - 1]
                lvl, ind = calc_lvl(strt)
            else:
                strt += steps[lvl - 1]
                lvl, ind = calc_lvl(strt)

        elif c == 'L':
            if strt % 2 != 0:
                continue
            strt -= steps[lvl - 2]
            lvl, ind = lvl - 1, 1

        else:
            if strt % 2 != 0:
                continue
            strt += steps[lvl - 2]
            lvl, ind = lvl - 1, 0

    print(strt)
