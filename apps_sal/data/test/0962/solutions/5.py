from collections import deque
import sys
sys.setrecursionlimit(10**6)

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

    def extract_cycle(self):
        self.seen = [0] * self.n
        self.checked = [0] * self.n
        self.hist = deque()
        self.node_in_cycle = -1

        def dfs(v):
            self.seen[v] = 1
            self.hist.append(v)
            for nv in self.adj[v]:
                if self.checked[nv]:
                    continue
                if self.seen[nv] and not self.checked[nv]:
                    self.node_in_cycle = nv
                    return
                dfs(nv)
                if self.node_in_cycle != -1:
                    return
            self.hist.pop()
            self.checked[v] = 1

        for i in range(self.n):
            if not self.checked[i]:
                dfs(i)
            if self.node_in_cycle != -1:
                break
        if self.node_in_cycle == -1:
            return []
        else:
            cycle = []
            while self.hist:
                t = self.hist.pop()
                cycle.append(t)
                if t == self.node_in_cycle:
                    break
            cycle.reverse()
            return cycle

n, m = [int(item) for item in input().split()]
edge = [[] for _ in range(n)]
for i in range(m):
    a, b = [int(item) - 1 for item in input().split()]
    edge[a].append(b)

DG = DirectedGraph(edge)
cycle = DG.extract_cycle()

if len(cycle) == 0:
    print(-1)
    return

while True:
    in_cycle = set(cycle)
    deg = [0] * n 
    for item in cycle:
        for v in edge[item]:
            if v in in_cycle:
                deg[v] += 1
    
    ok = True
    for i, item in enumerate(cycle):
        if deg[item] > 1:
            ok = False
            cur_id = start = i
    if ok:
        print(len(cycle))
        print("\n".join([str(item + 1) for item in cycle]))
        return

    ncycle = []
    cur = cycle[cur_id]
    while True:
        ncycle.append(cur)
        if cycle[start] in edge[cur]:
            break
        cur_id = (cur_id + 1) % len(cycle)
        cur = cycle[cur_id]
    cycle = ncycle[:]
