from sys import stdin, stdout
import math
from itertools import accumulate


def getabc(x1, y1, x2, y2):
    t1 = x2 - x1
    t2 = y2 - y1
    t3 = y1 * x2 - y2 * x1
    if t1 < 0:
        t1 = t1 * -1
        t2 = t2 * -1
        t3 = t3 * -1
    t4 = math.gcd(math.gcd(t1, t2), t3)
    return (t1 // t4, t2 // t4, t3 // t4)


n = int(stdin.readline())
x = []
y = []
for i in range(n):
    (xi, yi) = stdin.readline().strip().split(' ')
    x.append(int(xi))
    y.append(int(yi))
d = {}
there = {}
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        num = y[i] - y[j]
        den = x[i] - x[j]
        if num == 0:
            key = 'yintercept' + str(y[i])
            if key not in d:
                d[key] = 1
        elif den == 0:
            key = 'xintercept' + str(x[i])
            if key not in d:
                d[key] = 1
        else:
            (a, b, c) = getabc(x[i], y[i], x[j], y[j])
            key = str(a) + ' ' + str(b) + ' ' + str(c)
            keys = str(a) + ' ' + str(b)
            if key not in there:
                if keys in d:
                    d[keys] += 1
                else:
                    d[keys] = 1
                there[key] = 1
ansarr = [0, 0]
for i in d:
    if i[0] == 'x':
        ansarr[0] += 1
    elif i[0] == 'y':
        ansarr[1] += 1
    else:
        ansarr.append(d[i])
ans = 0
tarr = sum(ansarr)
for i in range(len(ansarr)):
    ans += (tarr - ansarr[i]) * ansarr[i]
stdout.write(str(ans // 2) + '\n')
