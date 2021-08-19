from functools import cmp_to_key
from math import atan2


def skal(a, b):
    return a[0][0] * b[0][0] + a[0][1] * b[0][1]


def vect(a, b):
    #print(a, b, a[0][0] * b[0][1] - b[0][0] * a[0][1])
    return a[0][0] * b[0][1] - b[0][0] * a[0][1]


def top(a):
    if a[0][1] < 0 or (a[0][1] == 0 and a[0][0] < 0):
        return 1
    else:
        return -1


def myfun(a, b):
    if top(a) != top(b):
        return top(a)

    if vect(a, b) > 0:
        return 1
    else:
        return -1


n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([[x, y], i + 1])
#a.sort(key = cmp_to_key(myfun))
a.sort(key=lambda x: atan2(x[0][1], x[0][0]))
a.append(a[0])
# print(a)
c = [[skal(a[0], a[1]), abs(vect(a[0], a[1]))], [a[0][1], a[1][1]]]
for i in range(1, n):
    d = [[skal(a[i], a[i + 1]), abs(vect(a[i], a[i + 1]))], [a[i][1], a[i + 1][1]]]
    if vect(d, c) > 0:
        c = d
print(c[1][0], c[1][1])

"""
3
1 -1
1 1 
-1 0

4
1 -1
1 1
-1 0
-1 -1
"""
