N, M = map(int, input().split())

graph = [[] for i in range(N)]
left = set()
right = set()
for i in range(M):
  l, r, d = map(int, input().split())
  l -= 1; r -= 1
  graph[l].append((r, d))
  graph[r].append((l, -d))
  left.add(l); right.add(r)

root = left - right
if M and len(root) == 0:
  print('No')
  return

X = [None] * N
while root:
  node = root.pop()
  X[node] = 0
  stack = [node]
  while stack:
    node = stack.pop()
    while graph[node]:
      child, d = graph[node].pop()
      if X[child] is None:
        X[child] = X[node] + d
        stack.append(child)
      elif X[child] != X[node] + d:
        print('No')
        return

print('Yes')
