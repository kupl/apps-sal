import sys
import collections
sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def S(): return input()


s = S()
gx, gy = Is()
l = s.split("T")
for i in range(len(l)):
    l[i] = len(l[i])
xlis, ylis = l[::2], l[1::2]
sx = xlis.pop(0) if len(xlis) > 0 else 0
sy = 0
xlis.sort(reverse=True)
ylis.sort(reverse=True)


def calc(start, goal, lis):
    p = start
    for e in lis:
        if p < goal:
            p += e
        else:
            p -= e
    return p == goal


if calc(sx, gx, xlis) and calc(sy, gy, ylis):
    print("Yes")
else:
    print("No")
