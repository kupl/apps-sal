import sys


def addEdge(n0, n1, graph):
    if (n0 in graph):
        graph[n0] = graph[n0] + [n1]
    else:
        graph[n0] = [n1]


def flatten(listOfLists):
    newlist = []
    for l in listOfLists:
        newlist = newlist + l
    return newlist


def zusKomp2(graph):
    nodes = list(graph.keys())
    zusKompn = {}
    for node in nodes:
        if node in flatten(list(zusKompn.values())):
            continue
        pointer = 0
        zusKompn[node] = [node]
        while pointer < len(zusKompn[node]):
            posNewNodes = graph[zusKompn[node][pointer]]
            for n in posNewNodes:
                if n not in zusKompn[node]:
                    zusKompn[node].append(n)
            pointer = pointer + 1

    return zusKompn


x = sys.stdin.read()
ls = x.splitlines()

ns, ms = ls[0].split()
n, m = int(ns), int(ms)

graph = {}

for l in ls[1:]:
    nodes = l.split()
    n0, n1 = int(nodes[0]), int(nodes[1])
    addEdge(n0, n1, graph)
    addEdge(n1, n0, graph)

isolatednodes = set(range(1, n + 1)) - set(graph.keys())
for i in isolatednodes:
    graph[i] = []

# print("graph:",graph)
# print("isoliert:",isolatednodes)
zusKompn = zusKomp2(graph)
# print("Zusammenhangskomponenten:",zusKompn)

print(2**(sum(list([len(x) - 1 for x in list(zusKompn.values())]))))
