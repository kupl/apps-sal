class Graph(object):
    """docstring for Graph"""

    def __init__(self, vertices):
        self.vertices = vertices
        graph = dict()
        for i in range(1, vertices + 1):
            graph[i] = []
        self.graph = graph

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def eulerPath(self):
        g = self.graph
        odd = [k for (k, v) in g.items() if len(v) % 2 == 1]
        if len(odd) == 0:
            odd = [list(g.keys())[0]]
        elif len(odd) == 1 or len(odd) > 2:
            return None
        path = []
        stack = [odd[-1]]
        while stack:
            u = stack[-1]
            if g[u]:
                v = g[u][0]
                del g[u][0]
                del g[v][g[v].index(u)]
                stack.append(v)
            else:
                path.append(stack.pop())
        return path


(n, e) = map(int, input().strip().split())
g = Graph(n)
u = []
v = []
for i in range(e):
    (a, b) = map(int, input().strip().split())
    g.add_edge(a, b)
    u.append(a)
    v.append(b)
ans = g.eulerPath()
if ans is None:
    print('NO')
elif len(ans) == e + 1 and ans[0] == ans[-1]:
    print('YES')
    temp_dict = {}
    for i in range(len(ans) - 1, 0, -1):
        if ans[i] in temp_dict:
            temp_dict[ans[i]][ans[i - 1]] = True
        else:
            temp_dict[ans[i]] = {ans[i - 1]: True}
    for i in range(e):
        if u[i] in temp_dict and v[i] in temp_dict[u[i]]:
            print(u[i], v[i])
        else:
            print(v[i], u[i])
else:
    print('NO')
