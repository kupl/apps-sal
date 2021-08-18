n, m = [int(item) for item in input().split()]
edge = [[] for _ in range(n)]
visited = [False] * n
raw = []
for i in range(m):
    a, b = [int(item) for item in input().split()]
    a -= 1
    b -= 1
    raw.append((a, b))
    edge[a].append(b)


class DirectedGraph:
    def __init__(self, adj):
        self.n = len(adj)
        self.adj = adj
        self.is_asyclic = False
        self.max_path_len = None

    def topological_sort(self):
        indegree = [0] * self.n
        for i, vs in enumerate(self.adj):
            for dest in vs:
                indegree[dest] += 1
        zero_v = []
        for v, indeg in enumerate(indegree):
            if indeg == 0:
                zero_v.append(v)
        max_path_len = 1
        tp_sorted = []
        to_be_added = []
        while True:
            while zero_v:
                v = zero_v.pop()
                tp_sorted.append(v)
                for dest in self.adj[v]:
                    indegree[dest] -= 1
                    if indegree[dest] == 0:
                        to_be_added.append(dest)
            if len(to_be_added) > 0:
                zero_v += to_be_added
                to_be_added = []
                max_path_len += 1
            else:
                break
        if len(tp_sorted) == self.n:
            self.is_asyclic = True
            self.max_path_len = max_path_len
            return tp_sorted
        else:
            self.is_asyclic = False
            return None


DG = DirectedGraph(edge)
tp_sorted = DG.topological_sort()
if DG.is_asyclic:
    print(1)
    print(" ".join(["1" for _ in range(m)]))
    return
else:
    print(2)
    ans = []
    for a, b in raw:
        if a > b:
            ans.append(1)
        else:
            ans.append(2)
    print(" ".join([str(item) for item in ans]))
