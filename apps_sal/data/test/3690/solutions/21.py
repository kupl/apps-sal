from math import *


def secs(h, m, s):
    return h * 60 * 60 + m * 60 + s


def chop():
    return (int(i) for i in input().split())


h, m, s, t1, t2 = chop()
sh = (h * 60 * 60 + m * 60 + s) % 43200
sm = (m * 60 + s) * 12 % 43200
ss = s * 720 % 43200
st1 = (t1 * 60 * 60) % 43200
st2 = (t2 * 60 * 60) % 43200
pr1 = []
st1, st2 = min(st1, st2), max(st1, st2)
for i in range(st1, st2 + 1):
    pr1.append(i)
pr2 = []
st1, st2 = max(st1, st2), min(st1, st2)
for i in range(st1, 43201):
    pr2.append(i)
for i in range(0, st2 + 1):
    pr2.append(i)
f1, f2 = False, False
if (sm in pr1) or (ss in pr1) or (sh in pr1):
    f1 = True
if (sm in pr2) or (ss in pr2) or (sh in pr2):
    f2 = True
if (f1) and (f2):
    print('NO')
else:
    print('YES')
