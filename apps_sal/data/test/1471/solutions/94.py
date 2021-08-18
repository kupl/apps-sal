

class Graph():

    def __init__(self):
        self.adjacency_dict = {}
        self.weight = []

    def add_vertex(self, v):
        self.adjacency_dict[v] = []
        self.weight.append([])

    def add_edge(self, v1, v2, w):
        self.adjacency_dict[v1].append(v2)
        self.adjacency_dict[v2].append(v1)
        self.weight[v1].append(w)
        self.weight[v2].append(w)

    def get_vertexes(self):
        return list(self.adjacency_dict.keys())

    def get_edges(self, v):
        return self.adjacency_dict[v], self.weight[v]

    def print_graph(self):
        print((self.adjacency_dict))


n = int(input())

res = []
g = Graph()
for i in range(n):
    res.append(-1)
    g.add_vertex(i)

for i in range(n - 1):
    u, v, w = list(map(int, input().strip().split()))
    g.add_edge(u - 1, v - 1, w % 2)

q = []
res[0] = 0
q.append(0)
while(len(q) > 0):
    v = q.pop()
    u_l, w_l = g.get_edges(v)
    for u, w in zip(u_l, w_l):
        if res[u] != -1:
            continue
        res[u] = (res[v] + w) % 2
        q.append(u)

for i in range(n):
    print((res[i]))
