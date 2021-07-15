def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  return path

dx = {}
nodes, edges = map(int, input().split(' '))
for c in range(edges+1):
    graph = {}
    for i in range(nodes):
      graph[i] = []
    dx[c] = graph


for i in range(edges):
  a, b, c = map(int, input().split(' '))
  dx[c][a-1].append(b-1)
  dx[c][b-1].append(a-1)

for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    t = 0
    for i in dx:
        graph = dx[i]
        
        if b-1 in iterative_bfs(graph, a-1):
            t += 1
    print(t)
