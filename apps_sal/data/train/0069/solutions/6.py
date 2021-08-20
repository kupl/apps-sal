import sys
import math


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def MI():
    return list(map(int, sys.stdin.readline().split()))


def SI():
    return sys.stdin.readline().strip()


t = II()
for q in range(t):
    (a, b) = MI()
    s = list(SI())
    x = []
    y = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if s[i - 1] == '0':
                y.append(0)
            else:
                y.append(1)
            x.append(count)
            count = 1
    if len(s) != 0 and s[-1] == '1':
        y.append(1)
        x.append(count)
    if len(y) != 0 and y[0] == 0:
        y.pop(0)
        x.pop(0)
    y1 = []
    ans = 0
    for i in range(len(y)):
        if y[i] == 0:
            y1.append(x[i])
        else:
            ans += a
    for i in y1:
        if i * b < a:
            ans -= a
            ans += i * b
    print(ans)
