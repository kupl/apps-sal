import math
import sys
import getpass
import bisect


def ria():
    return [int(i) for i in input().split()]


def gp(x1, y1, x2, y2, x3, y3):
    k = ((y2 - y1) * (x3 - x1) - (x2 - x1) * (y3 - y1)) / ((y2 - y1) ** 2 + (x2 - x1) ** 2)
    x4 = x3 - k * (y2 - y1)
    y4 = y3 + k * (x2 - x1)
    return (x4, y4)


files = True

if getpass.getuser().lower() == 'frohe' and files:
    sys.stdin = open('test.in')

n, m = ria()
ar = [0] * 400
st = [0] * 400
for i in range(n):
    a, b = ria()
    st[a] = 1
    for j in range(a + 1, b + 1):
        ar[j] = 1
if st[0] == 1 and sum(ar[1:m + 1]) == len(ar[1:m + 1]):
    print('YES')
else:
    print('NO')
