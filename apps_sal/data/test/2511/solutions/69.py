def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math

    #inf = 10**17
    mod = 10**9 + 7

    n,k = map(int, input().split())
    adj = [[] for _ in range(n)] #頂点数, 場合によって変える
    for _ in range(n-1):
        a,b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    def dfs(v, par, k):
        if par == -1:
            kk = k-1
        else:
            kk = k-2

        res = 1
        if v == 0:
            res *= k

        for i in range(len(adj[v])):
            nv = adj[v][i]
            if  nv == par:
                continue
            res *= kk * dfs(nv, v, k)
            res %= mod
            kk -= 1
        return res

    res = dfs(0, -1, k)
    print(res)

def __starting_point():
    main()
__starting_point()
