from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
EDGE = [tuple(map(int, input().split())) for i in range(m)]

E = [[] for i in range(n + 1)]


EDGEIN = [0] * (n + 1)
EDGEOUTLIST = [[] for i in range(n + 1)]
for x, y in EDGE:
    EDGEIN[y] += 1
    EDGEOUTLIST[x].append(y)

QUE = deque()

for i in range(1, n + 1):
    if EDGEIN[i] == 0:
        QUE.append(i)


TOP_SORT = []
while QUE:
    x = QUE.pop()
    TOP_SORT.append(x)
    for to in EDGEOUTLIST[x]:
        EDGEIN[to] -= 1
        if EDGEIN[to] == 0:
            QUE.appendleft(to)

if len(TOP_SORT) == n:
    print(1)
    print(*[1] * m)

else:
    print(2)
    for x, y in EDGE:
        if x > y:
            print(1, end=" ")
        else:
            print(2, end=" ")
