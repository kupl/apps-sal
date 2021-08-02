from collections import deque
import sys
mod = 10**9 + 7
input = sys.stdin.readline


class Graph(object):
    """docstring for Graph"""

    def __init__(self, n, d):  # Number of nodes and d is True if directed
        self.n = n
        self.graph = [[] for i in range(n)]
        self.parent = [-1 for i in range(n)]
        self.directed = d

    def addEdge(self, x, y):
        self.graph[x].append(y)
        if not self.directed:
            self.graph[y].append(x)

    def bfs(self, root):  # NORMAL BFS
        queue = [root]
        queue = deque(queue)
        vis = [0] * self.n
        while len(queue) != 0:
            element = queue.popleft()
            vis[element] = 1
            for i in self.graph[element]:
                if vis[i] == 0:
                    queue.append(i)
                    self.parent[i] = element
                    vis[i] = 1

    def dfs(self, root, vis):  # Iterative DFS
        stack = [root]
        stack2 = []
        while len(stack) != 0:  # INITIAL TRAVERSAL
            element = stack.pop()
            if vis[element]:
                continue
            vis[element] = 1
            stack2.append(element)
            for i in self.graph[element]:
                if vis[i] == 0:
                    self.parent[i] = element
                    stack.append(i)
        return stack2[::-1], vis

    def dfs2(self, root, vis):  # Iterative DFS
        stack = [root]
        stack2 = []
        cost = 10**18
        count = 0
        while len(stack) != 0:  # INITIAL TRAVERSAL
            element = stack.pop()
            if vis[element]:
                continue

            if costs[element] < cost:
                cost = costs[element]
                count = 1
            elif costs[element] == cost:
                count += 1
            vis[element] = 1
            stack2.append(element)
            for i in self.graph[element]:
                if vis[i] == 0:
                    self.parent[i] = element
                    stack.append(i)
        return cost, count, vis

    def count_scc(self, root):
        vis = [0] * self.n
        stack = []
        for i in range(self.n):
            if not vis[i]:
                a, vis = self.dfs(i, vis)
                stack.extend(a)

        g = [[] for i in range(self.n)]
        for i in range(self.n):
            for j in self.graph[i]:
                g[j].append(i)
        self.graph = g

        vis = [0] * self.n
        a1 = 0
        a2 = 1
        # print (stack)
        # print (self.graph)
        count = 0
        while len(stack) != 0:
            e = stack.pop()
            if not vis[e]:
                a, b, vis = self.dfs2(e, vis)
                a1 += a
                count += 1
                a2 = (a2 * b) % mod
            # print (vis)
        if a1 == 602483:
            print(count)
            print(vis)
            return

        return a1, a2


n, m = int(input()) + 1, 1000000007
q, p = [[] for i in range(n)], [[] for i in range(n)]
w = [0] + list(map(int, input().split()))
for i in range(int(input())):
    u, v = map(int, input().split())
    p[u].append(v)
    q[v].append(u)
r = set(i for i in range(1, n) if not p[i] or not q[i])
s, t = 0, 1
while r:
    i = r.pop()
    s += w[i]
    for j in p[i]:
        q[j].remove(i)
        if not q[j]: r.add(j)
    for j in q[i]:
        p[j].remove(i)
        if not p[j]: r.add(j)
r = set(i for i in range(1, n) if p[i] and q[i])
while r:
    i = r.pop()
    h = p[i]
    d, k = w[i], 1
    while h:
        i = h.pop()
        if not i in r: continue
        r.remove(i)
        h += p[i]
        if w[i] == d: k += 1
        elif w[i] < d: d, k = w[i], 1
    s += d
    t = (t * k) % m
print(s, t)
