"""
    Author      : Arif Ahmad
    Date        : 
    Algo        : 
    Difficulty  : 
"""
from sys import stdin, stdout


def main():
    n, k = [int(_) for _ in stdin.readline().strip().split()]
    a = [int(_) for _ in stdin.readline().strip().split()]

    cornerSlot = 2 * n
    middleSlot = 2 * n
    slotForOne = 0
    single = 0
    for x in a:
        req = x // 2
        #print('corner:', cornerSlot, ' middle:', middleSlot, ' single:', slotForOne)
        #print('group of:', x, ' req:', req, '\n')

        if req % 2 == 1:
            hand = 1
            req -= 1
        else:
            hand = 0

        # try to accommodate even no. of pairs in middle
        if middleSlot >= req:
            middleSlot -= req
            req = 0
        elif middleSlot > 0 and req > middleSlot:
            req -= middleSlot
            middleSlot = 0

        if hand:
            req += 1

        # now accommodate rest of the pairs in the corner
        if cornerSlot >= req:
            cornerSlot -= req
            req = 0
        elif cornerSlot > 0 and req > cornerSlot:
            req -= cornerSlot
            cornerSlot = 0

        # again, accommodate rest of the pairs in middle
        pairInMiddle = False
        if middleSlot >= req and (req > 0):
            middleSlot -= req
            req = 0
            pairInMiddle = True
        elif middleSlot > 0 and req > middleSlot:
            req -= middleSlot
            middleSlot = 0
            pairInMiddle = True

        if middleSlot % 2 == 1 and pairInMiddle:
            middleSlot -= 1
            slotForOne += 1

        #print('req now:', req)
        if x % 2 == 1:
            single += 1
        if req > 0:
            single += (req * 2)

        if single > 0:
            if slotForOne >= single:
                slotForOne -= single
                single = 0
            elif slotForOne > 0:
                single -= slotForOne
                slotForOne = 0

    total = cornerSlot + middleSlot
    while single > 0 and total > 0:
        total -= 1
        single -= 1

    if single:
        ans = 'NO'
    else:
        ans = 'YES'
    stdout.write(ans)


def __starting_point():
    main()


__starting_point()
