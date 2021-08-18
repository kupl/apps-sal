from sys import stdin
from collections import deque


INT_MAX = float('inf')


def shortest_cycle(gr):

    ans = INT_MAX

    for i in gr:

        dist = {x: int(1e9) for x in gr}

        par = {x: -1 for x in gr}

        dist[i] = 0
        q = deque()

        q.append(i)

        while q:

            x = q.popleft()

            for child in gr[x]:

                if dist[child] == int(1e9):

                    dist[child] = 1 + dist[x]

                    par[child] = x

                    q.append(child)

                elif par[x] != child and par[child] != x:
                    ans = min(ans, dist[x]
                              + dist[child] + 1)

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
        '''for x in graph:
            visited = {}
            q = deque()
            q.append((x,x,0))
            valid = False
            while q and not valid:
                n,p,d = q.popleft()
                if not n in visited:
                    visited[n] = d
                    for y in graph[n]:
                        if y != p:
                            if y in visited:
                                valid = d+visited[y]
                                break
                            else:
                                q.append((y,n,d+1))
            if valid:
                minC = min(minC,valid)
                minX = x
        if minC != float('inf'):
            print(minC+1)
        else:
            print(-1)'''
