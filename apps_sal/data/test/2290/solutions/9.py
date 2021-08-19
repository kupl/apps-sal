# @author

import sys


class DHarmoniousGraph:
    def solve(self):
        from collections import defaultdict

        class Node:
            def __init__(self, val):
                self.parent = self
                self.size = 1
                self.val = val

        def union(x, y):
            xRoot, yRoot = find(x), find(y)
            if xRoot == yRoot:
                return
            if xRoot.size >= yRoot.size:
                yRoot.parent = xRoot
                xRoot.size += yRoot.size
            else:
                xRoot.parent = yRoot
                yRoot.size += xRoot.size

        def find(x):
            while x.parent != x:
                x = x.parent
            return x

        n, m = [int(_) for _ in input().split()]
        adj = defaultdict(list)
        nodes = [Node(i) for i in range(n)]
        parent = [-1] * n
        for i in range(m):
            u, v = [int(_) for _ in input().split()]
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)
            union(nodes[u], nodes[v])

        for i in range(n):
            parent[i] = find(nodes[i]).val

        cc = defaultdict(tuple)

        for g in parent:
            cc[g] = (float('inf'), -float('inf'))

        for i in range(n):
            g = parent[i]
            cc[g] = (min(cc[g][0], i), max(cc[g][1], i))

        ccs = [[g, cc[g][0], cc[g][1]] for g in cc]
        ccs.sort(key=lambda x: x[1])

        ans = 0
        done = {g: 0 for g in cc}
        for g, cur, r in ccs:
            if done[g]:
                continue
            # print(g, cur, r, ans)
            while cur < r:
                cur_p = find(nodes[cur])
                r_p = find(nodes[r])
                # print(cur, r, cur_p.val, r_p.val)
                if cur_p != r_p:
                    ans += 1
                    done[cur_p.val] = 1
                    new_r = max(r, cc[cur_p.val][1])
                    union(nodes[cur], nodes[r])
                    r = new_r

                cur += 1

        print(ans)


solver = DHarmoniousGraph()
input = sys.stdin.readline

solver.solve()
