import sys
from collections import deque

sys.setrecursionlimit(10000)
INF = float('inf')

K = int(input())

# ある数に 1 を足すと各桁の和は 1 増える
# ある数に 10 を掛けると各桁の和は 0 増える
# mod K の世界で同じことやっても同じなので
# このグラフ上で 1 から 0 への最短距離が答え。

distances = [INF for _ in range(K)]

# 01BFS
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
