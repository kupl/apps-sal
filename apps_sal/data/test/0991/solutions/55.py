import sys
from heapq import *
input = sys.stdin.readline


def main():
    n, m, s = list(map(int, input().split()))
    
    s = min(s, 2500)
    
    railway = [[] for _ in range(n)]
    for i in range(m):
        u, v, a, b = list(map(int, input().split()))
        railway[u-1].append((v-1, a, b))
        railway[v-1].append((u-1, a, b))
    
    exchange = [None]*n
    for i in range(n):
        exchange[i] = tuple(map(int, input().split()))
    
    
    judge = [(0, 0, s)]
    heapify(judge)
    time = [[-1]*2501 for _ in range(n+1)]*n
    
    while judge:
        t, now, money = heappop(judge)
        if time[now][money] == -1:
            time[now][money] = t
        elif time[now][money] <= t:
            continue
        else:
            time[now][money] = min(time[now][money], t)
        
        if money < 2500:
            c, d = exchange[now]
            if time[now][min(2500, money+c)] == -1:
                heappush(judge, (t+d, now, min(2500, money+c)))
        for (v, a, b) in railway[now]:
            if money-a < 0:
                continue
            if time[v][money-a] == -1:
                heappush(judge, (t+b, v, money-a))
    
    for i in range(1, n):
        print((min(time[i])))
    
    
def __starting_point():
    main()

__starting_point()
