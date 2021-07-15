import sys
from collections import deque
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
U = 10 ** 5
edge = [[] for _ in range(2 * U + 1)]
for _ in range(N):
    x, y = map(int, input().split())
    y += U
    edge[x].append(y)
    edge[y].append(x)

ans = 0
seen = [False] * (2 * U + 1)
for i in range(1, 2 * U + 1):
    if not edge[i] or seen[i]:
        continue
    seen[i] = True
    node = deque([i])
    x = 0
    y = 0
    while node:
        s = node.popleft()
        if s <= U:
            x += 1
        else:
            y += 1
        for t in edge[s]:
            if seen[t]:
                continue
            seen[t] = True
            node.append(t)
    ans += x * y

ans = ans - N
print(ans)
