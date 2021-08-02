import sys
import heapq


class Node(object):
    def __init__(self, name):
        self.name = name
        self.minDistance = sys.maxsize
        self.paths = []
        self.baap = None

    def __lt__(self, other):
        return(self.minDistance < other.minDistance)


class Path(object):
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Dijkstra(object):
    def __init__(self, nodelist, start):
        self.nodelist = nodelist
        self.start = start

    def calculateShortestPath(self):
        queue = []
        self.nodelist[int(self.start) - 1].minDistance = 0
        heapq.heappush(queue, nodelist[int(self.start) - 1])
        while len(queue) > 0:
            actualNode = heapq.heappop(queue)
            for i in actualNode.paths:
                u = self.nodelist[int(i.start) - 1]
                v = self.nodelist[int(i.end) - 1]
                newdis = u.minDistance + i.weight
                if newdis < v.minDistance:
                    v.minDistance = newdis
                    v.baap = u
                    heapq.heappush(queue, v)

    def disp(self):
        arr = []
        for i in self.nodelist:
            arr.append(i.minDistance)
        return arr
# Dj till here


n, m, s, t = list(map(int, input().split(' ')))
n, m = int(n), int(m)
nodelist = []
for i in range(1, n + 1):
    nodelist.append(Node(str(i)))
pathdd = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(-1)
    pathdd.append(temp)
for i in range(m):
    st, en = input().split(' ')
    pathdd[int(st) - 1][int(en) - 1] = 1
    pathdd[int(en) - 1][int(st) - 1] = 1
    nodelist[int(st) - 1].paths.append(Path(st, en, 1))
    nodelist[int(en) - 1].paths.append(Path(en, st, 1))
dij = Dijkstra(nodelist, s)
dij.calculateShortestPath()
dn1 = dij.disp()  # minimum Distance of all nodes from source node
mindis = dn1[t - 1]
for i in nodelist:
    i.minDistance = sys.maxsize  # Reinitializing all distance to infinity
dij = Dijkstra(nodelist, t)
dij.calculateShortestPath()
dn2 = dij.disp()  # minimum distance of all nodes from target node
# print(dn1,"\n",dn2);
ctr = 0
for u in range(len(nodelist) - 1):
    for v in range(u + 1, len(nodelist)):
        if dn1[u] + 1 + dn2[v] >= mindis and dn1[v] + dn2[u] + 1 >= mindis and pathdd[u][v] == -1:
            ctr += 1
print(ctr)
