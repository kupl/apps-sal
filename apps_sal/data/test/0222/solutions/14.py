from math import *

strN = input()
n = int(strN)


def IsMatch(t):
    strT = str(t)
    if len(strN) == len(strT):
        if n == t: return 0
        else: return -1
    p = 0
    for c in strT:
        p = strN.find(c, p)
        if p == -1:
            break
        else:
            p += 1
    if p == -1:
        return -1
    else:
        return len(strN) - len(strT)


N = floor(sqrt(n))
for i in range(N, 0, -1):
    t = i * i
    d = IsMatch(t)
    if d >= 0:
        print(d)
        return
print(-1)
