import sys
import math
import fractions
from collections import deque
from collections import defaultdict
stdin = sys.stdin


def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


N, u, v = nm()
u = u - 1
v = v - 1
INF = 10**18
edge = [[] for i in range(N)]


def bfs(start, edge):
    d = [INF] * N
    d[start] = 0
    q = deque([start])
    while (q):
        e = q.popleft()
        for i in edge[e]:
            if(d[e] + 1 < d[i]):
                d[i] = d[e] + 1
                q.append(i)
    return d


for i in range(N - 1):
    A, B = nm()
    edge[B - 1].append(A - 1)
    edge[A - 1].append(B - 1)


d_A = bfs(u, edge)
d_B = bfs(v, edge)

ans = 0
for i in range(N):
    # if(d_A[0]%2==d_B[0]%2):
    #    continue
    # else:
    if(d_A[i] < d_B[i]):
        tmp = max(d_A[i], d_B[i])
        ans = max(ans, tmp)

print((ans - 1))
