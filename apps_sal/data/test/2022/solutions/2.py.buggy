from collections import deque
import sys
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

    def dfs(self, root, ans):  # Iterative DFS
        stack = [root]
        vis = [0] * self.n
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

        while len(stack2) != 0:  # BACKTRACING. Modify the loop according to the question
            element = stack2.pop()
            m = 0
            for i in self.graph[element]:
                if i != self.parent[element]:
                    m += ans[i]
            ans[element] = m
        return ans

    def shortestpath(self, source, dest):  # Calculate Shortest Path between two nodes
        self.bfs(source)
        path = [dest]
        while self.parent[path[-1]] != -1:
            path.append(parent[path[-1]])
        return path[::-1]

    def ifcycle(self):
        queue = [0]
        vis = [0] * n
        queue = deque(queue)
        while len(queue) != 0:
            element = queue.popleft()
            vis[element] = 1
            for i in self.graph[element]:
                if vis[i] == 1 and i != self.parent[element]:
                    s = i
                    e = element
                    path1 = [s]
                    path2 = [e]
                    while self.parent[s] != -1:
                        s = self.parent[s]
                        path1.append(s)
                    while self.parent[e] != -1:
                        e = self.parent[e]
                        path2.append(e)
                    for i in range(-1, max(-len(path1), -len(path2)) - 1, -1):
                        if path1[i] != path2[i]:
                            return path1[0:i + 1] + path2[i + 1::-1]
                if vis[i] == 0:
                    queue.append(i)
                    self.parent[i] = element
                    vis[i] = 1
        return -1

    def reroot(self, root, ans):
        stack = [root]
        vis = [0] * n
        while len(stack) != 0:
            e = stack[-1]
            if vis[e]:
                stack.pop()
                # Reverse_The_Change()
                continue
            vis[e] = 1
            for i in graph[e]:
                if not vis[e]:
                    stack.append(i)
            if self.parent[e] == -1:
                continue
            # Change_The_Answers()

    def dfss(self, root):

        vis = [0] * self.n
        color = [-1] * self.n
        color[root] = 0
        # self.pdfs(root,vis,color)
        # return
        stack = [root]
        while len(stack) != 0:
            e = stack.pop()
            if vis[e]:
                continue

            if color[e] == -1:
                if color[self.parent[e]]:
                    color[e] = 0
                    g1.append(e + 1)
                else:
                    color[e] = 1
                    g2.append(e + 1)
            vis[e] = 1

            for i in self.graph[e]:
                if not vis[i]:
                    stack.append(i)
                    self.parent[i] = e

        return


n, m, k = list(map(int, input().split()))
g = Graph(n, False)
for i in range(m):
    a, b = list(map(int, input().split()))
    g.addEdge(a - 1, b - 1)
l = g.ifcycle()
# print (l)
if l != -1 and len(l) <= k:
    print(2)
    print(len(l))
    for i in range(len(l)):
        l[i] += 1
    print(*l)
    return
g1, g2 = [1], []
g.dfss(0)
if len(g1) >= (k - 1) // 2 + 1:
    print(1)
    print(*g1[0:(k - 1) // 2 + 1])
else:
    print(1)
    print(*g2[0:(k - 1) // 2 + 1])
