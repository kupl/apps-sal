from math import *


def lcm(a, b):
    return a * b // gcd(a, b)


(a, b) = list(map(int, input().split()))
(a, b) = (min(a, b), max(a, b))
diff = b - a
if b % a == 0:
    print(0)
else:
    divs = set()
    for i in range(1, int(diff ** (1 / 2)) + 1):
        if diff % i == 0:
            divs.add(i)
            divs.add(diff // i)
    curLCM = None
    curK = None
    for can in divs:
        if b % can == 0:
            tLCM = lcm(b, a)
            tk = 0
        else:
            x = b // can
            x = (x + 1) * can
            tk = x - b
            tLCM = lcm(b + tk, a + tk)
        if curK == None:
            (curK, curLCM) = (tk, tLCM)
        elif curLCM > tLCM:
            (curK, curLCM) = (tk, tLCM)
        elif curLCM == tLCM:
            curK = min(tk, curK)
    print(curK)
