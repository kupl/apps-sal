import getpass
import sys
import math


def ria():
    return [int(i) for i in input().split()]


files = True

if getpass.getuser() == 'frohenk' and files:
    sys.stdin = open("test.in")

n = ria()[0]
ar = ria()
st = input()
zer = True
l, r = 0, 0
mx = 0
mn = 200020
changable = [False] * n
for i in range(len(st)):
    if st[i] == '0':

        if not zer:
            if l + 1 > mn or r + 1 < mx:
                print('NO')
                return
        mx = 0
        mn = 200020
        zer = True
        continue
    if zer:
        l = i
    r = i + 1
    mx = max(mx, ar[i])
    mx = max(mx, ar[i + 1])
    mn = min(mn, ar[i])
    mn = min(mn, ar[i + 1])
    changable[i] = True
    changable[i + 1] = True

    zer = False
# print(changable)
for n, i in enumerate(ar):
    if (n + 1) != i and not changable[n]:
        print('NO')
        return
print('YES')
