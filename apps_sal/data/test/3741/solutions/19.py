from sys import stdin
from collections import deque
INT_MAX = float('inf')


def shortest_cycle(gr):
    ans = INT_MAX
    for i in gr:
        dist = {x: int(1000000000.0) for x in gr}
        par = {x: -1 for x in gr}
        dist[i] = 0
        q = deque()
        q.append(i)
        while q:
            x = q.popleft()
            for child in gr[x]:
                if dist[child] == int(1000000000.0):
                    dist[child] = 1 + dist[x]
                    par[child] = x
                    q.append(child)
                elif par[x] != child and par[child] != x:
                    ans = min(ans, dist[x] + dist[child] + 1)
    if ans == INT_MAX:
        return -1
    else:
        return ans


n = int(stdin.readline())
a = sorted([int(x) for x in stdin.readline().split()])
if n - a.count(0) > 128:
    print(3)
else:
    l = [[] for x in range(64)]
    mini = False
    for x in a:
        c = 1
        for y in range(64):
            if x & c:
                l[y].append(x)
                if len(l[y]) > 2:
                    mini = True
            c <<= 1
    if mini:
        print(3)
    else:
        minC = float('inf')
        minX = -1
        flatL = set()
        for x in l:
            for y in x:
                flatL.add(y)
        graph = {}
        for x in flatL:
            graph[x] = set()
            for y in flatL:
                if y != x and y & x:
                    graph[x].add(y)
        print(shortest_cycle(graph))
        "for x in graph:\n            visited = {}\n            q = deque()\n            q.append((x,x,0))\n            valid = False\n            while q and not valid:\n                n,p,d = q.popleft()\n                if not n in visited:\n                    visited[n] = d\n                    for y in graph[n]:\n                        if y != p:\n                            if y in visited:\n                                valid = d+visited[y]\n                                break\n                            else:\n                                q.append((y,n,d+1))\n            if valid:\n                minC = min(minC,valid)\n                minX = x\n        if minC != float('inf'):\n            print(minC+1)\n        else:\n            print(-1)"
