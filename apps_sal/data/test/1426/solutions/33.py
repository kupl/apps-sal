import sys
from collections import deque

def main():
  input = sys.stdin.readline
  n, m = map(int, input().split())
  roads0 = [[] for _ in range(n)]
  roads1 = [[] for _ in range(n)]
  roads2 = [[] for _ in range(n)]
  
  for i in range(m):
    u, v = map(int, input().split())
    roads0[u-1].append(v-1)
    roads1[u-1].append(v-1)
    roads2[u-1].append(v-1)
  

  s, t = map(int, input().split())
  not_yet = deque([])
  already = [[False]*3 for _ in range(n)]
  dist = [[0]*3 for _ in range(n)]
  for v in roads0[s-1]:
    not_yet.append((v, 1))
    dist[v][1] = 1
    already[v][1] = True
  already[s-1][0] = True
  while not_yet:
    key = not_yet.popleft()
    k1, k2 = key[0], key[1]
    if k2 == 0:
      for v in roads1[k1]:
        if already[v][1]:
          continue
        dist[v][1] = dist[k1][0]+1
        already[v][1] = True
        not_yet.append((v, 1))
    elif k2 == 1:
      for v in roads2[k1]:
        if already[v][2]:
          continue
        dist[v][2] = dist[k1][1]+1
        already[v][2] = True
        not_yet.append((v, 2))
    else:
      for v in roads0[k1]:
        if already[v][0]:
          continue
        dist[v][0] = dist[k1][2]+1
        already[v][0] = True
        not_yet.append((v, 0))
  if already[t-1][0]:
    print(dist[t-1][0]//3)
  else:
    print(-1)
  
    
def __starting_point():
  main()
__starting_point()
