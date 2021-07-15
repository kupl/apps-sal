def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

x = []
sa = int(input())
toed = list(map(int, input().split(' ')))
for i in range(sa):
    x.append(input())

graph = {}
for i in range(sa):
    graph[i] = []

marked = [False] * sa

for bad in range(sa):
    for asdf in range(bad+1, sa):
        if x[bad][asdf] == '1':
            graph[bad].append(asdf)
            graph[asdf].append(bad)

done = []
for i in range(sa):
  if not marked[i]:
      a = recursive_dfs(graph, i)
      done.append(a)
      for j in recursive_dfs(graph, i):
          marked[j] = True

final = [0] * sa

for i in done:
    o = [toed[a] for a in i]
    o.sort()
    i.sort()
    for a in range(len(i)):
        final[i[a]] = o[a]

print(' '.join([str(i) for i in final]))

