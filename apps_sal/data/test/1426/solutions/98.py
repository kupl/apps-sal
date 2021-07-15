def main():
  N, M = map(int, input().split())
  edge = [[[] for _ in range(3)] for _ in range(N)]
  for i in range(M):
    u, v = map(int, input().split())
    edge[u-1][0].append([v-1,1])
    edge[u-1][1].append([v-1,2])
    edge[u-1][2].append([v-1,0])
  d = [[-1]*3 for _ in range(N)]
  S, T = map(int, input().split())
  d[S-1][0] = 0
  que = [[S-1, 0]]
  while len(que)>0:
    now = que.pop(0)
    for nex in edge[now[0]][now[1]]:
      if d[nex[0]][nex[1]] != -1:continue
      d[nex[0]][nex[1]] = d[now[0]][now[1]]
      if now[1] == 2:
        d[nex[0]][nex[1]] += 1
      que.append(nex)
  print(d[T-1][0])
  
def __starting_point():
  main()
__starting_point()
