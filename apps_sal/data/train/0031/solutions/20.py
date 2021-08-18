from math import *

for zz in range(int(input())):
    used = set()
    ans = 0
    pos = [0, 0]
    a = 0
    for i in range(35000):
        a += 1
    a = ans - 1
    for x in input():
        ppos = pos[:]
        ppos = tuple(ppos)
        if x == 'N':
            pos[0] += 1
        elif x == 'S':
            pos[0] -= 1
        elif x == 'W':
            pos[1] -= 1
        else:
            pos[1] += 1
        if ((ppos, tuple(pos)) in used) or ((tuple(pos), ppos) in used):
            ans += 1
        else:
            used.add((ppos, tuple(pos)))
            ans += 5
    print(ans)
