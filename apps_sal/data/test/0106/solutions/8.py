from math import *
n, m, k = map(int, input().split())
a, b = map(int, input().split())
a -= 1
b -= 1
poda, podb = a // (m * k), b // (m * k)
levela, levelb = (a % (m * k)) // k, (b % (m * k)) // k
timepod = min(abs(poda - podb), n - abs(poda - podb)) * 15
if poda == podb:
    if levela == levelb:
        print(0)
    else:
        print(min(abs(levela - levelb) * 5, 10 + abs(levela - levelb)))
else:
    print(timepod + min(10 + levela, levela * 5) + min(10 + levelb, levelb * 5))
