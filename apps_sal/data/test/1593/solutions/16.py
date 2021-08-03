from math import *
def R(): return map(int, input().split())


n, s = R()
x = sorted((x * x + y * y, k) for x, y, k in (R() for i in range(n)))
for i in range(n):
    s += x[i][1]
    if s >= 1000000:
        print(sqrt(x[i][0]))
        return
print(-1)
