import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
EDGE = [list(map(int, input().split())) for i in range(m)]

EDGELIST = [[] for i in range(n + 1)]

for x, y in EDGE:
    EDGELIST[x].append(y)
    EDGELIST[y].append(x)

QUE = deque([[1, 1]])
ANS = [-1] * (n + 1)
ANS[1] = 1


while QUE:
    x, color = QUE.pop()
    ANS[x] = color

    for to in EDGELIST[x]:
        if ANS[to] == color:
            print("NO")
            return

        if ANS[to] == -1:
            QUE.appendleft([to, abs(color - 1)])


print("YES")
for x, y in EDGE:
    if ANS[x] == 1:
        print("1", end="")
    else:
        print("0", end="")
