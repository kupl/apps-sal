import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def main():

    def bfs(u):
        dist = [inf] * n
        cur = [u]
        pre = [-1] * n
        dist[u] = 0
        d = 0
        while cur:
            d += 1
            nxt = []
            for v in cur:
                for kv in to[v]:
                    if dist[kv] != inf:
                        continue
                    dist[kv] = d
                    pre[kv] = v
                    nxt.append(kv)
            cur = nxt
        mn = [inf, -1]
        for v in range(n):
            if v == u:
                continue
            if u in to[v]:
                mn = min(mn, [dist[v], v])
        res = []
        v = mn[1]
        if mn[0] == inf:
            return [0] * (n + 1)
        for _ in range(mn[0] + 1):
            res.append(v)
            v = pre[v]
        return res
    inf = 10 ** 9
    (n, m) = list(map(int, input().split()))
    to = defaultdict(set)
    for _ in range(m):
        (u, v) = list(map(int, input().split()))
        to[u - 1].add(v - 1)
    ans = [0] * (n + 1)
    for u in range(n):
        res = bfs(u)
        if len(res) < len(ans):
            ans = res
    if len(ans) == n + 1:
        print(-1)
    else:
        print(len(ans))
        for u in ans:
            print(u + 1)


main()
