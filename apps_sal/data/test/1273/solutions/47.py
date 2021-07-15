from collections import defaultdict

N = int(input())
P = [[] for _ in range(N)]
AB = defaultdict(int)

for _ in range(N-1):
  a, b = [int(x)-1 for x in input().split()]
  P[a].append(b)
  P[b].append(a)
  AB[(a, b)] = -1

C = [-1] * N

def bfs(s):
    d = [-1] * N
    d[s] = 0
    p_old = [s]
    K = -1
    while p_old:
      p_new = []
      for i in p_old:
        c = 1
        for j in P[i]:
          if d[j] != -1:
            continue
          if C[i] == c:
            c += 1
          d[j] = 0
          p_new.append(j)
          C[j] = c
          AB[(i, j)] = c
          K = max(K, c)
          c += 1
      p_old = p_new
    return K

print((bfs(0)))

for x in list(AB.values()):
  print(x)

