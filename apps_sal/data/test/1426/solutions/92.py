import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
import queue

N, M = list(map(int, input().split()))
if M == 0:
    print((-1))
    return
adj = [[] for _ in range(N)]
for i in range(M):
    u, v = list(map(int, input().split()))    
    u -= 1
    v -= 1
    adj[u].append(v)
S, T = list(map(int, input().split()))
S -= 1
T -= 1

dist = [[INF,INF,INF] for _ in range(N+1)]
 
q = queue.Queue()
q.put((S, 0))
dist[S][0] = 0
while not q.empty():
    u, l = q.get()
    for v in adj[u]:
        nl = (l + 1) % 3
        if dist[v][nl] != INF:
            continue
        dist[v][nl] = dist[u][l] + 1
        q.put((v, nl))
d = dist[T][0]
answer = -1 if d == INF else d // 3
print(answer)



