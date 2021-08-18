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
        self.parent = [-1 for i in range(self.n)]
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

    def dfs(self, root, ans):
        stack = [root]
        vis = [0] * self.n
        stack2 = []
        while len(stack) != 0:
            element = stack.pop()
            order.append(element)
            if vis[element]:
                continue
            vis[element] = 1
            stack2.append(element)
            temp = []
            for i in self.graph[element]:
                if vis[i] == 0:
                    temp.append(i)
            temp.sort(reverse=True)
            for i in temp:
                stack.append(i)

        while len(stack2) != 0:
            element = stack2.pop()
            m = 0
            for i in self.graph[element]:
                if i != self.parent[element]:
                    m += ans[i]
            ans[element] = m + 1
        return ans

    def shortestpath(self, source, dest):
        self.bfs(source)
        path = [dest]
        while self.parent[path[-1]] != -1:
            path.append(parent[path[-1]])
        return path[::-1]

    def ifcycle(self):
        self.bfs(0)
        queue = [0]
        vis = [0] * n
        queue = deque(queue)
        while len(queue) != 0:
            element = queue.popleft()
            vis[element] = 1
            for i in graph[element]:
                if vis[i] == 1 and i != parent[element]:
                    return True
                if vis[i] == 0:
                    queue.append(i)
                    vis[i] = 1
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


n, q = list(map(int, input().split()))
g = Graph(n, False)
g.parent = [-1] + list(map(int, input().split()))
for i in range(1, n):
    g.parent[i] -= 1
    g.addEdge(g.parent[i], i)
count = [0] * n
order = []
g.dfs(0, count)
rank = {}
for i in range(n):
    rank[order[i]] = i
for i in range(q):
    a, k = list(map(int, input().split()))
    if k > count[a - 1]:
        print(-1)
    else:
        print(order[rank[a - 1] + k - 1] + 1)
