def main():

    from bisect import bisect_left as bl, bisect_right as br, insort
    import sys
    import math
    from collections import defaultdict as dd, deque
    def data(): return sys.stdin.readline().strip()
    def mdata(): return list(map(int, data().split()))
    out = sys.stdout.write
    INF = float("INF")
    mod = int(1e9) + 7

    def kosaraju():
        stack = []
        s = []
        vis = [0] * n
        for i in range(n):
            if vis[i] == 0:
                s.append(i)
                while s:
                    a = s[-1]
                    if vis[a] == 1:
                        stack.append(s.pop())
                        vis[a] = 2
                        continue
                    elif vis[a] == 2:
                        s.pop()
                        continue
                    vis[a] = 1
                    for i in g[a]:
                        if vis[i] == 0:
                            s.append(i)
        stack = stack[::-1]
        comp = []
        vis = [0] * n
        ans1 = 0
        ans2 = 1
        for i in stack:
            if vis[i] == 0:
                d = dd(int)
                s.append(i)
                while s:
                    a = s[-1]
                    if vis[a] == 1:
                        d[c[s.pop()]] += 1
                        vis[a] = 2
                        continue
                    elif vis[a] == 2:
                        s.pop()
                        continue
                    vis[a] = 1
                    for i in g1[a]:
                        if vis[i] == 0:
                            s.append(i)
                min1 = min(d.keys())
                ans1 += min1
                ans2 = (ans2 * d[min1]) % mod
        return ans1, ans2

    n = int(data())
    c = mdata()
    m = int(data())
    g = [set() for i in range(n)]
    g1 = [set() for i in range(n)]
    for i in range(m):
        u, v = mdata()
        g[u - 1].add(v - 1)
        g1[v - 1].add(u - 1)
    ans1, ans2 = kosaraju()
    print(ans1, ans2)


def __starting_point():
    main()


__starting_point()
