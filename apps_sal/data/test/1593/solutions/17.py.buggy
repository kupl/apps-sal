from math import *
def R(): return map(int, input().split())


n, s = R()
x = sorted((hypot(x, y), k) for x, y, k in (R() for i in range(n)))
for t in x:
    s += t[1]
    if s >= 1000000:
        print(t[0])
        return
print(-1)
