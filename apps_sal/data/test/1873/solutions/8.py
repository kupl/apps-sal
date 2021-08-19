from bisect import *


def inpList():
    return list(map(int, input().split()))


def inp():
    return int(input())


(n, m) = inpList()
a = inpList()
x = {}
for i in range(1, m + 1):
    x[i] = 0
for i in a:
    x[i] += 1
p = sum((x[i] for i in x))
t = sum((x[i] * x[i] for i in x))
print((p * p - t) // 2)
