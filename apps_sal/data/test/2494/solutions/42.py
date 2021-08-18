import sys
from collections import deque

sys.setrecursionlimit(10000)
INF = float('inf')

K = int(input())


distances = [INF for _ in range(K)]

remains = deque()
remains.append((1, 1))
while distances[0] == INF:
    d, mod_k = remains.popleft()
    distances[mod_k] = d
    if distances[(mod_k + 1) % K] == INF:
        remains.append((d + 1, (mod_k + 1) % K))
    if distances[mod_k * 10 % K] == INF:
        remains.appendleft((d, mod_k * 10 % K))
print((distances[0]))
