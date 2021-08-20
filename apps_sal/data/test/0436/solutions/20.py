import math
import sys
import collections


def getdict(n):
    d = {}
    if type(n) is list:
        for i in n:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    else:
        for i in range(n):
            t = ii()
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
    return d


def cdiv(n, k):
    return n // k + (n % k != 0)


def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(map(int, input().split()))


n = ii()
d = li()
a = d[0]
s = sum(d)
r = [1]
dr = [a]
for i in range(1, n):
    if d[i] <= a // 2:
        r.append(i + 1)
        dr.append(d[i])
if sum(dr) > sum(d) // 2:
    print(len(r))
    print(' '.join(map(str, r)))
else:
    print(0)
