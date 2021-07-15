MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from collections import deque

def main():
    n,m = map(int,input().split())
    G = [[] for _ in range(3*n)]
    for _ in range(m):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        for i in range(3):
            G[u*3 + i].append(v*3 + (i + 1)%3)
    
    s,g = map(int,input().split())
    s -= 1
    g -= 1

    q = deque([3*s])
    dist = [-1] * (3*n)
    dist[3*s] = 0
    while q:
        p = q.popleft()
        for e in G[p]:
            if dist[e] < 0:
                dist[e] = dist[p] + 1
                q.append(e)
                
    print(dist[3*g]//3 if dist[3*g] >= 0 else -1)
def __starting_point():
    main()
__starting_point()
