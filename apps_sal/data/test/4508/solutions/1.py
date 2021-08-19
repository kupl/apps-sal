import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())
EDGE = [list(map(int, input().split())) for i in range(N - 1)]

EDGELIST = [[] for i in range(N + 1)]

for i, j in EDGE:
    EDGELIST[i].append(j)
    EDGELIST[j].append(i)

#EDGES=[[] for i in range(N+1)]
REDG = [None for i in range(N + 1)]
QUE = deque([1])
check = [0] * (N + 1)
DEPTH = [None] * (N + 1)
i = 0
while QUE:
    NQUE = deque()
    i += 1

    while QUE:
        x = QUE.pop()
        DEPTH[x] = i
        check[x] = 1
        for to in EDGELIST[x]:
            if check[to] == 1:
                continue
            else:
                # EDGES[x].append(to)
                REDG[to] = x
                NQUE.append(to)
    QUE = NQUE


check = [0] * (N + 1)
check[1] = 1
# NEXT=[]

# for i in EDGES[1]:
#    check[i]=1
#    NEXT.append(i)

# for j in NEXT:
#    for k in EDGES[j]:
#        check[k]=1


LEAF = []
for i in range(2, N + 1):
    if len(EDGELIST[i]) == 1:
        LEAF.append((-DEPTH[i], i))

QUE = LEAF
heapq.heapify(QUE)
ANS = 0

# print(check,QUE)

while QUE:
    dep, x = heapq.heappop(QUE)
    if check[x] != 0 or dep >= -3:
        continue

    if check[REDG[x]] == 2:
        continue

    if check[x] == 0:
        check[x] = 1
    if check[REDG[REDG[x]]] == 0:
        check[REDG[REDG[x]]] = 1
    check[REDG[x]] = 2
    heapq.heappush(QUE, (-DEPTH[REDG[REDG[REDG[x]]]], REDG[REDG[REDG[x]]]))
    ANS += 1

    # print(x,QUE,check)

print(ANS)
