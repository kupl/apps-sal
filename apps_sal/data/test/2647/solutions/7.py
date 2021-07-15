from collections import deque
H, W = list(map(int, input().split()))
route = []
n_black = 0
for _ in range(H):
  tmp_ls = input()
  n_black += tmp_ls.count("#")
  route.append(tmp_ls)
visited = [[False]*W for _ in range(H)]
dist = [[-1]*W for _ in range(H)]
dist[0][0] = 0
tmp = [0,0]
goal = [H-1, W-1]
kouho = deque()
def rinsetsu(ls):
  x, y = ls[0], ls[1]
  ans = []
  if x-1 >= 0:
    ans.append([x-1, y])
  if x+1 <= H-1:
    ans.append([x+1, y])
  if y-1 >= 0:
    ans.append([x, y-1])
  if y+1 <= W-1:
    ans.append([x, y+1])
  return ans
for ls in rinsetsu([0,0]):
  if route[ls[0]][ls[1]] == ".":
    kouho.append([ls[0], ls[1], 0, 0])
def bfs():
  while True:
    while True:
      if len(kouho) == 0:
        return
      tmp = kouho.popleft()
      if not visited[tmp[0]][tmp[1]]:
        break
    x, y = tmp[0], tmp[1]
    visited[x][y] = True
    dist[x][y] = dist[tmp[2]][tmp[3]] + 1
    if [x, y] == goal:
      return
    for ls in rinsetsu([x,y]):
      if not visited[ls[0]][ls[1]] and route[ls[0]][ls[1]] == ".":
        kouho.append(ls + [x, y])
bfs()
if dist[H-1][W-1] == -1:
  print((-1))
else:
  white = dist[H-1][W-1] + 1
  print((H*W - white - n_black))


