from types import GeneratorType
n, k = list(map(lambda x: int(x), input().split()))
m = list(map(lambda x: int(x), input().split()))


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    @bootstrap
    def DFSUtil(self, temp, v, visited):

        visited[v] = True

        for i in self.adj[v]:
            if visited[i] == False:
                yield self.DFSUtil(temp, i, visited)

        temp.append(v)
        yield temp

    def addEdge(self, v, w):
        self.adj[v].append(w)

    @bootstrap
    def isCyclicUtil(self, v, visited, recStack):

        visited[v] = True
        recStack[v] = True

        for neighbour in self.adj[v]:
            if visited[neighbour] == False:
                ans = yield self.isCyclicUtil(neighbour, visited, recStack)
                if ans == True:
                    yield True
            elif recStack[neighbour] == True:
                yield True

        recStack[v] = False
        yield False

    def isCyclic(self, nodes):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in nodes:
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


G = Graph(n)

for i in range(0, n):

    x = list(map(lambda x: int(x), input().split()))
    if x[0] == 0:
        continue
    else:
        for k in range(1, x[0] + 1):
            G.addEdge(i, x[k] - 1)
visited = [False for _ in range(n)]

path = []
for subj in m:
    temp = []
    if visited[subj - 1] == False:

        G.DFSUtil(temp, subj - 1, visited)

        path.extend(temp)
if G.isCyclic([x - 1 for x in m]):
    print(-1)
else:
    print(len(path))
    for p in path:
        print(p + 1, end=" ")
    print()
