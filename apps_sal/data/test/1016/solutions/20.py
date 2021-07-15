def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def iterative_dfs(graph, start, path=[]):
  '''iterative depth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path

def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  return path

nodes, edges = list(map(int, input().split(' ')))
graph = {}
for i in range(nodes):
  graph[i] = []

for i in range(edges):
  a, b = list(map(int, input().split(' ')))
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

marked = [False] * nodes
num = 0
for i in range(nodes):
  if not marked[i]:
    for j in recursive_dfs(graph, i):
      marked[j] = True
    num += 1

print(2**(nodes-num))
##graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
##graph = {0: [1, 4, 5, 9], 1: [0, 2, 4, 6, 8], 2: [1, 3, 5, 7, 8], 3: [2, 7, 9], 4: [0, 1, 9], 5: [0, 2, 9], 6: [1, 9], 7: [2, 3, 9], 8: [1, 2], 9: [0, 3, 4, 5, 6, 7]}
##graph = {'A':['B'], 'B':['A', 'C'], 'C':['B', 'D'], 'D':['C', 'E'], 'E':['D'], 'F':['G'], 'G':['F']}
##print('recursive dfs ', recursive_dfs(graph, 'A'))
##print('iterative dfs ', iterative_dfs(graph, 'A'))
##print('iterative bfs ', iterative_bfs(graph, 'A'))

