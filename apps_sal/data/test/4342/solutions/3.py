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
            m = [0, 0]
            for i in self.graph[element]:
                if i != self.parent[element]:
                    m[0] += ans[i][0]
                    m[1] += ans[i][1]
            if arr[element] == 1:
                m[0] += 1
            elif arr[element] == 2:
                m[1] += 1
            ans[element] = m
        return ans

    def shortestpath(self, source, dest):  # Calculate Shortest Path between two nodes
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
        count = 0
        vis = [0] * self.n
        while len(stack) != 0:
            e = stack[-1]
            # print (e,ans)
            if vis[e]:
                stack.pop()
                if self.parent[e] != -1:
                    ans[self.parent[e]][0] += ans[e][0]
                    ans[self.parent[e]][1] += ans[e][1]
                    if self.parent[self.parent[e]] != -1:
                        ans[self.parent[e]][0] -= ans[self.parent[self.parent[e]]][0]
                        ans[self.parent[e]][1] -= ans[self.parent[self.parent[e]]][1]
                continue
            vis[e] = 1
            for i in self.graph[e]:
                if not vis[i]:
                    stack.append(i)
            if self.parent[e] == -1:
                continue
            ans[self.parent[e]][0] -= ans[e][0]
            ans[self.parent[e]][1] -= ans[e][1]
            if self.parent[self.parent[e]] != -1:
                ans[self.parent[e]][0] += ans[self.parent[self.parent[e]]][0]
                ans[self.parent[e]][1] += ans[self.parent[self.parent[e]]][1]
            if 0 in ans[e] and 0 in ans[self.parent[e]]:
                count += 1
        return count


n = int(input())
g = Graph(n, False)
arr = list(map(int, input().split()))
for i in range(n - 1):
    x, y = list(map(int, input().split()))
    g.addEdge(x - 1, y - 1)
ans = [[0, 0] for i in range(n)]
a = g.dfs(0, ans)
print(g.reroot(0, a))
