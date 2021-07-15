from functools import *
from operator import *
import sys, threading

def work() :
    sys.setrecursionlimit(1 << 18)

    n = int(input())
    a = [0] + list(map(int, input().split()))
    tota = sum(a)
    adj = [[] for _ in range(n + 1)]

    totsz = [0] * (n + 1)
    totw = [0] * (n + 1)
        
    def dfs(u, p) :
        totsz[u] = a[u]
        for v in adj[u] :
            if v == p : 
                continue
            dfs(v, u)
            totsz[u] += totsz[v]
            totw[u] += totw[v] + totsz[v]

    def dfs2(u, p, w) :
        totw[u] += w
        for v in adj[u] :
            if v == p : 
                continue
            dfs2(v, u, totw[u] - totw[v] - totsz[v] + tota - totsz[v])

    for _ in range(n - 1) :
        u, v = list(map(int, input().split()))
        adj[u].append(v)
        adj[v].append(u)

    dfs(1, 0)
    dfs2(1, 0, 0)
    print(max(totw))

def __starting_point():
    sys.setrecursionlimit(200050)
    threading.stack_size(80000000)
    thread = threading.Thread(target=work)
    thread.start()

__starting_point()
