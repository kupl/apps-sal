import sys
import string


def ria():
    return [int(i) for i in input().split()]


n = ria()[0]
ar1 = ria()
ar2 = ria()
p1 = 0
p2 = 0
ar1.sort()
ar2.sort()
ar1 = [i for i in reversed(ar1)]
ar2 = [i for i in reversed(ar2)]
# print(ar1, ar2)

pp1 = 0
pp2 = 0
for i in range(n):
    if pp1 < n:
        if pp2 >= n or ar1[pp1] >= ar2[pp2]:
            p1 += ar1[pp1]
            pp1 += 1
        else:
            pp2 += 1
    elif pp2 < n:
        pp2 += 1

    if pp2 < n:
        if pp1 >= n or ar1[pp1] <= ar2[pp2]:
            p2 += ar2[pp2]
            pp2 += 1
        else:
            pp1 += 1
    elif pp1 < n:
        pp1 += 1

print(p1 - p2)
