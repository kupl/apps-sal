from collections import deque
import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
E = [list(map(int, input().split())) for i in range(m)]
cost = [0] * (n + 1)
EDGELIST = [[] for i in range(n + 1)]
for (x, y) in E:
    cost[x] += 1
    cost[y] += 1
    EDGELIST[x].append(y)
    EDGELIST[y].append(x)
x = cost.index(max(cost))
QUE = deque([x])
check = [0] * (n + 1)
ANS = []
while QUE:
    x = QUE.popleft()
    check[x] = 1
    for to in EDGELIST[x]:
        if check[to] == 0:
            ANS.append([x, to])
            QUE.append(to)
            check[to] = 1
for (x, y) in ANS:
    print(x, y)
