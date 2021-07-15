def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def conn(x, y):
    a, b = x[0], x[1]
    c, d = y[0], y[1]
    return c < a < d or c < b < d

adj = {}
vert = []
n = int(input())
for i in range(n):
    a, b, c = list(map(int, input().split(' ')))
    if a == 1:
        incoming = (b, c)
        adj[incoming] = []
        for vertex in vert:
            if conn(vertex, incoming):
                adj[vertex].append(incoming)
            if conn(incoming, vertex):
                adj[incoming].append(vertex)
        vert.append(incoming)
        
    if a == 2:
        check = vert[b-1]
        in_chk = vert[c-1]
        if in_chk in recursive_dfs(adj, check):
            print("YES")
        else:
            print("NO")

