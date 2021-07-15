from collections import deque, namedtuple
from heapq import *
from sys import stdin

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges, bi=True):
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))
        self.edges = [make_edge(*edge) for edge in edges]
        self.vertices = set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            ))
        self.neighbors = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            self.neighbors[edge.start].add(edge.end)

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if[edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        distances[source] = 0

        q, seen = [(0, source)], set()
        while q:
            (curr_cost, current_vertex) = heappop(q)
            if current_vertex in seen:
                continue
            seen.add(current_vertex)
            for neighbor in self.neighbors[current_vertex]:
                cost = 1
                if neighbor in seen:
                    continue
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbor]:
                    distances[neighbor] = alternative_route
                    heappush(q, (alternative_route, neighbor))

        return distances


n, m, s, t = [int(x) for x in stdin.readline().rstrip().split()]

verts = []
for i in range(m):
    verts.append(tuple([int(x) for x in stdin.readline().rstrip().split()]))
rev_verts = []
for i in verts:
    rev_verts.append((i[1], i[0]))
for i in rev_verts:
    verts.append(i)
graph = Graph(verts)
s_dist = graph.dijkstra(s, t)
t_dist = graph.dijkstra(t, s)
SHORTEST_DIST = s_dist[t]
count = 0

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if j not in graph.neighbors[i] and \
                i not in graph.neighbors[j] and \
                s_dist[i] + t_dist[j] + 1 >= SHORTEST_DIST and \
                s_dist[j] + t_dist[i] + 1 >= SHORTEST_DIST:
            count = count + 1

print(count)

