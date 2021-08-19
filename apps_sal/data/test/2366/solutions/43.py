import collections
import math


def cmb_factorial(s):
    return math.factorial(s) // (math.factorial(2) * math.factorial(s - 2))


n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
f = {}
cmb = 0
for x in c.values():
    f[1] = 0
    f[2] = 1
    if x >= 3:
        f[x] = cmb_factorial(x)
        if x - 1 not in f:
            f[x - 1] = cmb_factorial(x - 1)
    cmb += f.get(x)
for z in a:
    y = c.get(z)
    ans = cmb
    if y >= 2:
        ans = cmb - f.get(y) + f.get(y - 1)
    print(ans)
