from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
answers = ['respectable', 'ugly']

ps = []

for _ in range(8):
    x, y = input().split(' ')
    ps.append(Point(int(x), int(y)))

ps.sort()

def parallelline(lA, lB):
    pAA, pAB, pAC = lA
    pBA, pBB, pBC = lB
    if pAA.x == pAB.x and pAA.x == pAC.x:
        if pBA.x == pBB.x and pBA.x == pBC.x:
            if pAA.y == pBA.y and pAB.y == pBB.y and pAC.y == pBC.y:
                if pAA.y != pAB.y and pAA.y != pAC.y:
                   return True
    if pAA.y == pAB.y and pAA.y == pAC.y:
        if pBA.y == pBB.y and pBA.y == pBC.y:
            if pAA.x == pBA.x and pAB.x == pBB.x and pAC.x == pBC.x:
                if pAA.x != pAB.x and pAA.x != pAC.x:
                     return True
    return False

if parallelline((ps[0], ps[1], ps[2]), (ps[5], ps[6], ps[7])) and parallelline((ps[0], ps[3], ps[5]), (ps[2], ps[4], ps[7])):
    print(answers[0])
else:
    print(answers[1])

