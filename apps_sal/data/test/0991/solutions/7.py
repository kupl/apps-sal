from heapq import heappop, heappush

import sys
def input():return sys.stdin.readline().strip()

def main():
    N, M, S = map(int, input().split())
    to = [{} for _  in range(N)]
    for _ in range(M):
        u, v, a, b = map(int, input().split())
        u -= 1
        v -= 1
        to[u][v] = (a, b)
        to[v][u] = (a, b)
    info = tuple(tuple(map(int, input().split())) for _ in range(N))

    MAX_SILVER = 50 * (N-1)
    INF = 10 ** 18
    # dijkstra (time, vertex, money)
    visited = [[False]*(MAX_SILVER+1) for _ in range(N)]
    cost = [[INF]*(MAX_SILVER+1) for _ in range(N)]
    q = []
    S = min(S, MAX_SILVER)
    heappush(q, (0, 0, S)) # (time, vertex, silver)

    while q:
        t, now, s = heappop(q)
        if visited[now][s]:continue
        visited[now][s] = True
        cost[now][s] = t

        # next node
        for nv, (a, b) in to[now].items():
            nt = t + b
            rest = s - a
            if rest >= 0:
                if cost[nv][rest] <= nt : continue 
                heappush(q, (nt, nv, rest))
        
        # exchange gold with silver
        rate, time = info[now]
        nt = t + time
        ns = min(s+rate, MAX_SILVER)
        if cost[now][ns] <= nt : continue
        heappush(q, (nt, now, ns))
        
    
    for i in range(1, N):
        print(min(cost[i]))

def __starting_point():
    main()
__starting_point()
