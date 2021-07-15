import sys
from collections import defaultdict, deque
readline = sys.stdin.readline
N = int(readline())
P = defaultdict(list); Q = defaultdict(list)
for i in range(N):
    x, y = map(int, readline().split())
    P[x].append(y)
    Q[y].append(x)
X = set(); Y = set()

res = 0
que = deque()
for x in P:
    que.append((0, x))
    X.add(x)
    cx = 1; cy = 0
    while que:
        t, v = que.popleft()
        if t:
            for x in Q[v]:
                if x in X:
                    continue
                X.add(x)
                que.append((0, x))
                cx += 1
        else:
            for y in P[v]:
                if y in Y:
                    continue
                Y.add(y)
                que.append((1, y))
                cy += 1
    res += cx * cy
print(res - N)
