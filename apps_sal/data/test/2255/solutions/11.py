import sys
import heapq
input = sys.stdin.readline
(n, m) = map(int, input().split())
EDGE = [list(map(int, input().split())) for i in range(m)]
EDGELIST = [[] for i in range(n + 1)]
for (x, y) in EDGE:
    EDGELIST[x].append(y)
    EDGELIST[y].append(x)
NOW = EDGELIST[1]
heapq.heapify(NOW)
check = [0] * (n + 1)
ANS = [1]
check[1] = 1
while NOW:
    x = heapq.heappop(NOW)
    if check[x] == 1:
        continue
    else:
        ANS.append(x)
        check[x] = 1
        for e in EDGELIST[x]:
            if check[e] == 0:
                heapq.heappush(NOW, e)
for a in ANS:
    print(a, end=' ')
