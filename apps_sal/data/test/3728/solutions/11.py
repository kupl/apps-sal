import sys
import re
import itertools
def rai(x): return list(map(int, x.split()))


def pm(a):
    for l in a:
        print(l)
    print()


_use_stdin = True
if _use_stdin:
    inp = sys.stdin
else:
    inp = open("input.txt", "r")
ls = inp.read().splitlines()
n, m = rai(ls[0])
a = [rai(l) for l in ls[1:]]
b = list(range(1, m + 1))
c = []


def f(x):
    t = 0
    for i, x in enumerate(a[x]):
        if x != b[i]:
            t += 1
    return t


flag = False
for i in range(m):
    for j in range(i, m):
        for k in range(n):
            a[k][i], a[k][j] = a[k][j], a[k][i]
        flag2 = True
        for k in range(n):
            if f(k) > 2:
                flag2 = False
                break
#         for k in range(n):
#             print(a[k], f(k))
#         print()
        if not flag:
            flag = flag2
        for k in range(n):
            a[k][i], a[k][j] = a[k][j], a[k][i]
print("YES" if flag else "NO")
