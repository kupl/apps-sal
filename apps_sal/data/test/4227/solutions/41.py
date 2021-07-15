N, M = map(int, input().split())
D = {}
for i in range(M):
  a, b = map(int, input().split())
  if a not in D:
    D[a] = set()
  if b not in D:
    D[b] = set()
  D[a].add(b)
  D[b].add(a)
if 1 not in D or len(D) != N:
  print(0)
else:
  S = set(D.keys())
  ans = 0
  task = [(1, set())]
  while len(task) > 0:
    pos = 0
    log = set()
    pos, log = task.pop(0)
    log.add(pos)
    for i in D[pos]:
      if i not in log:
        task.append((i, log.copy()))
    else:
      if log == S:
        ans += 1
  print(ans)
