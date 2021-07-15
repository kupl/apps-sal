n, m = list(map(int, input().split()))
has_cat = [None] + [x == 1 for x in map(int, input().split())]

neighbors = [[] for i in range(n + 1)]
for i in range(n - 1):
  u, v = list(map(int, input().split()))
  neighbors[u].append(v)
  neighbors[v].append(u)

seen = [False for i in range(n + 1)]

count = 0

queue = [(0, 1)]
tail = 0
while tail < len(queue):
  cats, u = queue[tail]
  tail += 1
  seen[u] = True
  if has_cat[u]:
    cats += 1
    if cats > m:
      continue
  else:
    cats = 0

  is_leaf = True
  for v in neighbors[u]:
    if not seen[v]:
      is_leaf = False
      queue.append((cats, v))

  if is_leaf:
    count += 1

print(count)


