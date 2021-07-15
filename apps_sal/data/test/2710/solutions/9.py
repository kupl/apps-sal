"""
Author: Andrew Jakubowicz
Problem: Soldier and Traveling
link: http://codeforces.com/problemset/problem/546/E#

n cities and m roads.
Each city has an army.

i-th city has a_i soldiers.

Soldiers can move at **most** one road or stay put.



"""
import math

class Edge:
    def __init__(self, cap, flow, target, rev = None):
        self.capacity = cap
        self.flow = flow
        self.target = target
        # Reversed edges have capacity of 0
        self.rev = rev

    def __repr__(self):
        return "<e: (cap: {}, target: {}, flow: {}>".format(self.capacity, self.target, self.flow)


def dfs(u, t, bottleneck, visited, graph):
    if u == t:
        return bottleneck
    visited[u] = True
    for e in graph[u]:
        residual = e.capacity - e.flow
        if residual > 0 and not visited[e.target]:
            augment = dfs(e.target,t, min(bottleneck, residual), visited, graph)
            if augment > 0:
                e.flow += augment
                e.rev.flow -= augment
                return augment
    return 0

def ford_fulkerson(g, s, t):
    """
    Solves maximum flow problem.
    :param g: graph
    :param s: start
    :param t: end
    :return: flow
    """
    flow = 0
    while True:
        Visited = [False for _ in range(len(g))]
        augment = dfs(s,t, math.inf , Visited, g)
        flow += augment
        if augment <= 0:
            break

    return flow

def print_graph(graph):
    for i, edges in enumerate(graph):
        print("{}: [{}]".format(i, edges))


def __starting_point():

    [n,m] = list(map(int, input("").split()))

    city_soldiers = list(map(int, input("").split()))
    want_soldiers = list(map(int, input("").split()))


    # index 0 is start. Index 2n+1 is sink node.
    graph = [[] for _ in range(2*n+2)]

    # Source to initial cities.
    for i,soldiers in enumerate(city_soldiers):
        graph[0].append(Edge(soldiers, 0, i+1))

    # Set up edges to sink.
    for i,soldiers in enumerate(want_soldiers):
        graph[n+i+1].append(Edge(soldiers,0,2*n+1))

    # Set up paths
    for _ in range(m):
        [s,t] = list(map(int, input("").split()))
        graph[t].append(Edge(1000, 0, n+s))
        graph[s].append(Edge(1000, 0, n+t))

    # Set up staying soldiers.
    for i in range(n):
        i = i+1
        graph[i].append(Edge(city_soldiers[i-1], 0, n+i))

    # Create residual graph
    residualGraph = [[] for _ in range(len(graph))]
    # Generate the residual network
    for u, edges in enumerate(graph):
        for e in edges:
            target = e.target
            # Circular link
            reverse = Edge(0, 0, u, e)
            e.rev = reverse

            residualGraph[u].append(e)
            residualGraph[target].append(reverse)

    flow = ford_fulkerson(residualGraph, 0, 2*n+1)
    if sum(want_soldiers) != flow or sum(city_soldiers) != sum(want_soldiers):
        print("NO")
    else:
        print("YES")
        adjmatrix = [[0 for _ in range(n)] for _ in range(n)]

        for u, edges in enumerate(residualGraph[1:2* n + 1]):
            u = u+1
            for e in edges:
                if e.capacity == 1000 or (u+n == e.target and e.target != 2*n+1):
                    adjmatrix[u-1][e.target-n-1] = e.flow


        for row in adjmatrix:
            print(" ".join(map(str, row)))


__starting_point()
