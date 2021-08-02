from collections import deque
import sys
from decimal import Decimal

readline = sys.stdin.readline
n = int(input())
edges = [[] * n for _ in [None] * n]

for _ in [None] * (n - 1):
    a, b = map(int, readline().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

visited = [False] * n
visited[0] = True
cnt = 0
total = 0
dq = deque()
append, pop = dq.append, dq.popleft
append((0, 0, Decimal(1)))

while dq:
    pos, l, multiple = pop()
    flag = True
    to = [x for x in edges[pos] if visited[x] == False]

    if to:
        x = len(to)
        multiple /= Decimal(x)
        for v in to:
            visited[v] = True
            append((v, l + 1, multiple))
    else:
        total += Decimal(l) * multiple

print(total)
