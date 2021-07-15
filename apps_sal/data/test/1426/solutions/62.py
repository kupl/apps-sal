def solve():
  N, M = map(int, input().split(' '))
  G = [[] for _ in range(N + 10)]
  dist = [[-1 for _ in range(3)] for _ in range(N + 10)]
  for _ in range(M):
    u, v = map(int, input().split(' '))
    G[u].append(v)
  S, T = map(int, input().split(' '))
  que = [[S, 0]]
  dist[S][0] = 0
  while que:
    q = que.pop(0)
    nv, np = q[0], q[1]
    for item in G[nv]:
      if dist[item][(np + 1) % 3] == -1:
        que.append([item, (np + 1) % 3])
        dist[item][(np + 1) % 3] = dist[nv][np] + 1
  if dist[T][0] == -1:
    return -1
  else:
    return dist[T][0] // 3
print(solve())
