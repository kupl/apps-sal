from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.parentColor = [-1] * (n + 1)
        self.color = [-1] * (n + 1)
        self.visited = [False] * (n + 1)
        self.n = n

    def addEdge(self, fr, to):
        self.graph[fr].append(to)
        self.graph[to].append(fr)

    def BFS(self, root):
        queue = deque()
        queue.append(root)
        self.color[root] = 1
        self.parentColor[root] = 0
        while(queue):
            s = queue.popleft()
            Set = defaultdict(bool)
            Set[self.color[s]] = True
            Set[self.parentColor[s]] = True
            culur = 1
            for i in self.graph[s]:
                if(self.visited[i] == False):
                    queue.append(i)
                    self.parentColor[i] = self.color[s]
                    while(1):
                        if(not Set[culur]):
                            self.color[i] = culur
                            culur += 1
                            break
                        culur += 1
            self.visited[s] = True

    def show(self):
        print(max(self.color))
        print(*self.color[1:])


n = int(input())
G = Graph(n)
for _ in range(n - 1):
    a, b = map(int, input().split())
    G.addEdge(a, b)
G.BFS(1)
G.show()
