import sys
from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self, v, visited, parent):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, v) == True:
                    return True

            elif i != parent:
                return True

        return False

    def isTree(self):
        visited = [False] * self.V

        if self.isCyclicUtil(0, visited, -1) == True:
            return False

        for i in range(self.V):
            if visited[i] == False:
                return False

        return True


def main():
    s = sys.stdin.readline().split()
    n, m = int(s[0]), int(s[1])
    graph = Graph(n)
    for _ in range(m):
        s = sys.stdin.readline().split()
        graph.addEdge(int(s[0]) - 1, int(s[1]) - 1)

    return "yes" if graph.isTree() else "no"


def __starting_point():
    sys.stdout.write(main())


__starting_point()
