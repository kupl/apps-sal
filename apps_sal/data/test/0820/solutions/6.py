from bisect import *


def inpList():
    return list(map(int, input().split()))


def inp():
    return int(input())


n = inp()
m = inp()
a = []
for i in range(n):
    a.append(inp())
a.sort()
a.reverse()
for i in range(1, n):
    a[i] += a[i - 1]
print(bisect_left(a, m) + 1)
