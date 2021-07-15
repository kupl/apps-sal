

import sys

inf = float('inf')
sys.setrecursionlimit(100000)

class Graph(object):
  def __init__(self, v):
    self.edges = {}
    self.vertex_map = [[False for j in range(v+1)] for i in range(v+1)]

  def add_edge(self, u, v):
    edges, vertex_map = self.edges, self.vertex_map
    if not u in edges: edges[u] = []
    if not v in edges: edges[v] = []
    edges[u].append(v)
    edges[v].append(u)
    vertex_map[u][v] = vertex_map[v][u] = True

  def has_edge(self, u, v):
    edges, vertex_map = self.edges, self.vertex_map
    return self.vertex_map[u][v]

  def adj(self, u):
    edges, vertex_map = self.edges, self.vertex_map
    return [] if not u in edges else edges[u]

def dfs(graph, u, visited, rps):
  adju = graph.adj(u)
  ret = inf
  if len(adju) == 0 or visited[u]: return ret
  visited[u] = True
  # puts "visited: #{u} #{adju}"
  for v in adju:
    if visited[v]: continue
    r = dfs(graph, v, visited, rps)
    if ret > r: ret = r
  for v in adju:
    ae = set(adju) & set(graph.adj(v)) - set([u, v])
    if len(ae) == 0: continue
    for p in ae:
      if not visited[v]: continue
      if ret > rps[u] + rps[v] + rps[p] - 6:
        # print(u, v, p, graph.adj(u), graph.adj(v), graph.adj(p), rps[u], rps[v], rps[p])
        ret = rps[u] + rps[v] + rps[p] - 6
  return ret

def algo():
  vc, lc = [int(i) for i in input().split(' ')]
  graph = Graph(vc)
  rps = [0 for i in range(vc+1)]
  for i in range(1, lc+1):
    u, v = [int(i) for i in input().split(' ')]
    graph.add_edge(u, v)
    rps[u] += 1
    rps[v] += 1
  ret = inf
  visited = [False for i in range(vc+1)]
  for u in range(1, vc+1):
    r = dfs(graph, u, visited, rps)
    if ret > r: ret = r
  if ret == inf: ret = -1
  print(ret)

algo()

