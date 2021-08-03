INF = 10**5


class Graph:

    def __init__(self, vertices):

        self.vertices = vertices
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)]

    def BFS(self, s, t, parent):

        visited = [False for i in range(self.vertices)]
        queue = []

        visited[s] = True
        queue.append(s)

        while len(queue) > 0:

            vertex = queue.pop(0)

            for i, value in enumerate(self.graph[vertex]):
                if not visited[i] and value > 0:
                    queue.append(i)
                    parent[i] = vertex
                    visited[i] = True

                    if i == t:
                        return True

        return False

    def max_flow(self):

        flow = 0
        parent = [i for i in range(self.vertices)]

        while self.BFS(0, self.vertices - 1, parent):

            min_flow = INF
            t = self.vertices - 1
            while t != 0:
                min_flow = min(min_flow, self.graph[parent[t]][t])
                t = parent[t]

            flow += min_flow

            t = self.vertices - 1

            while t != 0:

                self.graph[parent[t]][t] -= min_flow
                self.graph[t][parent[t]] += min_flow
                t = parent[t]

        return flow


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

edges = {}
for i in range(m):
    x, y = map(int, input().split())
    edges[(x, y)] = True

g = Graph(2 * n + 2)  # s -> 0 , a[i], b[i], t-> 2n+1

for i in range(1, n + 1):
    g.graph[0][i] = a[i - 1]

for x, y in edges:
    g.graph[x][y + n] = INF
    g.graph[y][x + n] = INF

for i in range(1, n + 1):
    g.graph[i + n][2 * n + 1] = b[i - 1]

for i in range(1, n + 1):
    g.graph[i][i + n] = a[i - 1]

max_flow = g.max_flow()
if max_flow == sum(a) and sum(a) == sum(b):
    print("YES")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and (edges.get((j, i), False) or edges.get((i, j), False)):
                print(10**5 - g.graph[i][j + n], end=" ")
            elif i != j:
                print(0, end=" ")
            else:
                print(a[i - 1] - g.graph[i][i + n], end=" ")
        print()

else:
    print("NO")
