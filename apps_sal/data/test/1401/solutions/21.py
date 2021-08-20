from collections import deque
import sys
input = sys.stdin.readline


class Graph(object):
    """docstring for Graph"""

    def __init__(self, n, d):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.parent = [-1 for i in range(n)]
        self.directed = d

    def addEdge(self, x, y):
        self.graph[x].append(y)
        if not self.directed:
            self.graph[y].append(x)

    def bfs(self, root):
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
                    dist[i] = dist[element] + w[element, i]

    def bfs2(self, root):
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
                    minn[i] = min(minn[element], dist[i])

    def bfs3(self, root):
        queue = [root]
        queue = deque(queue)
        vis = [0] * self.n
        count = 0
        while len(queue) != 0:
            element = queue.popleft()
            vis[element] = 1
            count += 1
            for i in self.graph[element]:
                if vis[i] == 0 and remove[i] == 0:
                    queue.append(i)
                    self.parent[i] = element
                    vis[i] = 1
        return count

    def dfs(self, root, ans):
        stack = [root]
        vis = [0] * self.n
        stack2 = []
        while len(stack) != 0:
            element = stack.pop()
            if vis[element]:
                continue
            vis[element] = 1
            stack2.append(element)
            for i in self.graph[element]:
                if vis[i] == 0:
                    self.parent[i] = element
                    stack.append(i)
        while len(stack2) != 0:
            element = stack2.pop()
            m = 0
            for i in self.graph[element]:
                if i != self.parent[element]:
                    m += ans[i]
            ans[element] = m
        return ans

    def shortestpath(self, source, dest):
        self.bfs(source)
        path = [dest]
        while self.parent[path[-1]] != -1:
            path.append(parent[path[-1]])
        return path[::-1]

    def detect_cycle(self):
        indeg = [0] * self.n
        for i in range(self.n):
            for j in self.graph[i]:
                indeg[j] += 1
        q = deque()
        vis = 0
        for i in range(self.n):
            if indeg[i] == 0:
                q.append(i)
        while len(q) != 0:
            e = q.popleft()
            vis += 1
            for i in self.graph[e]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        if vis != self.n:
            return True
        return False

    def reroot(self, root, ans):
        stack = [root]
        vis = [0] * n
        while len(stack) != 0:
            e = stack[-1]
            if vis[e]:
                stack.pop()
                continue
            vis[e] = 1
            for i in graph[e]:
                if not vis[e]:
                    stack.append(i)
            if self.parent[e] == -1:
                continue


n = int(input())
a = list(map(int, input().split()))
g = Graph(n, False)
w = {}
for i in range(n - 1):
    (x, y) = map(int, input().split())
    w[i + 1, x - 1] = y
    w[x - 1, i + 1] = y
    g.addEdge(i + 1, x - 1)
dist = [0] * n
minn = [0] * n
g.bfs(0)
g.bfs2(0)
remove = [0] * n
for i in range(1, n):
    if dist[i] - minn[i] > a[i]:
        remove[i] = 1
print(n - g.bfs3(0))
