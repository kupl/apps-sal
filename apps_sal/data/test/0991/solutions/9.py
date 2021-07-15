import sys
import heapq
def input(): return sys.stdin.readline().rstrip()


n, m, s = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

maxcoin = 0

for i in range(m):
    u, v, a, b = list(map(int, input().split()))
    graph[u].append((v, a, b))
    graph[v].append((u, a, b))
    maxcoin += a

ryougae = [0, 0]*(n+1)

for i in range(1, n+1):
    c, d = list(map(int, input().split()))
    ryougae[i] = [c, d]


mindist = [[10**20]*(maxcoin+1) for _ in range(n+1)]
hq = []
heapq.heappush(hq, (0, 1, min(maxcoin, s)))
while hq:
    minute, city, coin = heapq.heappop(hq)
    if mindist[city][coin] != 10**20:
        continue
    mindist[city][coin] = minute
    for i, pay, length in graph[city]:
        if coin >= pay:
            if mindist[i][coin-pay] != 10**20:
                continue
            heapq.heappush(hq, (minute+length, i, coin-pay))
    if coin < maxcoin:
        kankin = min(maxcoin, ryougae[city][0]+coin)
        if mindist[city][kankin] != 10**20:
            continue
        heapq.heappush(hq, (minute+ryougae[city][1], city, kankin))

for i in range(2, n+1):
    print((min(mindist[i])))

