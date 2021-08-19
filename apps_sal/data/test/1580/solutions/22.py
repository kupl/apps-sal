class Graph:

    def __init__(self):
        self.adjacency_dict = {}

    def add_vertex(self, v):
        self.adjacency_dict[v] = []

    def add_edge(self, v1, v2):
        self.adjacency_dict[v1].append(v2)
        self.adjacency_dict[v2].append(v1)

    def remove_edge(self, v1, v2):
        self.adjacency_dict[v1].remove(v2)
        self.adjacency_dict[v2].remove(v1)

    def remove_vertex(self, v):
        while self.adjacency_dict[v] != []:
            adjacency_vertex = self.adjacency_dict[v][-1]
            self.remove_edge(v, adjacency_vertex)
        del adjacency_vertex[v]

    def get_vertexes(self):
        return list(self.adjacency_dict.keys())

    def get_edges(self, v):
        return self.adjacency_dict[v]

    def print_graph(self):
        print(self.adjacency_dict)


(n, m) = list(map(int, input().strip().split()))
xyz = [list(map(int, input().strip().split())) for _ in range(m)]
g = Graph()
for i in range(n):
    g.add_vertex(i)
for i in range(m):
    g.add_edge(xyz[i][0] - 1, xyz[i][1] - 1)
res = 0
reached_nodes = [0 for _ in range(n)]
for i in g.get_vertexes():
    if reached_nodes[i] == 1:
        continue
    res += 1
    reached_nodes[i] = 1
    q = [i]
    while len(q) > 0:
        u = q.pop()
        for v in g.get_edges(u):
            if reached_nodes[v] == 1:
                continue
            q.append(v)
            reached_nodes[v] = 1
print(res)
