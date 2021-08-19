import threading
import sys
sys.setrecursionlimit(10 ** 9)
threading.stack_size(67108864)


def main():
    (n, m) = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    graph = {int(x) + 1: [] for x in range(n)}
    for i in range(m):
        (ff, sf) = [int(x) for x in input().split()]
        graph[ff].append(sf)
        graph[sf].append(ff)
    comps = {}
    cl = [-1] * n

    def dfs(v, c, p):
        cl[v - 1] = c
        if c not in comps:
            comps[c] = []
        comps[c].append(v)
        for i in graph[v]:
            if i != p:
                if cl[i - 1] == -1:
                    dfs(i, c, v)
    cc = 1
    for i in range(n):
        if cl[i] == -1:
            dfs(i + 1, cc, -1)
            cc += 1
    price = 0
    for i in comps:
        minp = 999999999999999
        for j in comps[i]:
            minp = min(c[j - 1], minp)
        price += minp
    print(price)


thread = threading.Thread(target=main)
thread.start()
