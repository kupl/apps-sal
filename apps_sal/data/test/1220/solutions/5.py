import sys
import math
import os.path

FILE_INPUT = "e.in"
DEBUG = os.path.isfile(FILE_INPUT)
if DEBUG:
    sys.stdin = open(FILE_INPUT)


def ni():
    return list(map(int, input().split()))


def nia():
    return list(map(int, input().split()))


def log(x):
    if (DEBUG):
        print(x)


n, m = ni()
a = [{i} for i in range(n)]
for _ in range(m):
    x, y = ni()
    x, y = x - 1, y - 1
    a[x].add(y)
    a[y].add(x)

q = []
willVisit = set(range(n))
while willVisit:
    x = willVisit.pop()
    queue = [x]
    count = 1
    while queue:
        y = queue.pop()
        sibling = willVisit - a[y]
        count += len(sibling)
        queue.extend(sibling)
        willVisit &= a[y]
    q.append(count)

q.sort()
print(len(q))
print(" ".join(map(str, q)))
