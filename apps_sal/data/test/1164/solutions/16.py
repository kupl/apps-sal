from math import *

def remd(x):
    y = []
    for i in x:
        if i != '.':
            y.append(i)
    return ''.join(y)

def parse(x):
    if '.' not in x:
        return int(x)
    i = len(x) - 1
    cnt = 0
    while x[i] != '.':
        i -= 1
        cnt += 1
    if cnt == 2:
        x1 = int(remd(x[:i]))
        x2 = int(x[i + 1:])
        return x1 + x2 / 100
    else:
        return int(remd(x))

def format(y):
    y1 = int(y)
    y2 = round((y - y1) * 100)

    y1 = str(y1)
    yy = []
    for i in range(len(y1)):
        yy.append(y1[len(y1) - 1 - i])
        if i % 3 == 2 and i != len(y1) - 1:
            yy.append('.')
    yy.reverse()
    yy = ''.join(yy)

    if y2 != 0:
        yy += '.'
        yy += ('%02d' % y2)
    return yy

s = input()
pr = []
cur = []
for i in s:
    if '0' <= i <= '9' or i == '.':
        cur.append(i)
    else:
        if len(cur) > 0:
            pr.append(''.join(cur))
            cur = []
if len(cur) > 0:
    pr.append(''.join(cur))

sm = 0
for i in pr:
    sm += parse(i)
print(format(sm))
