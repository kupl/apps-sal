n, m = list(map(int, input().split()))

neighbors = {}
for _ in range(m):
  a, b = list(map(int, input().split()))
  if a not in list(neighbors.keys()):
    neighbors.update({a:set()})
  if b not in neighbors[a]:
    neighbors[a].add(b)
  if b not in list(neighbors.keys()):
    neighbors.update({b:set()})
  if a not in neighbors[b]:
    neighbors[b].add(a)
#print(neighbors)
lst = [0] * (n - 1) #部屋１を除く、すべての部屋の通り方を調べる、「通っていない」を0として定義
visited = set() #一度訪れた部屋は再度探索する必要はないので、それを省くための集合
queue = [[0, set([1])]]
while queue:
  #print(queue)
  pre_room, rooms = queue.pop(0) #左が今いる部屋、右が次に進む部屋
  #print(pre_room, rooms)
  for room in rooms:
    if room in visited:
      continue
    if lst[room - 2] == 0 and room != 1: #次に進む部屋が通っていないかどうか（と今いる部屋が１ではないこと）の確認
      lst[room - 2] = pre_room #部屋2の場合、lstのindexは0に相当するので-2する必要がある
    visited.add(room) #今いる部屋を訪れたので、集合に入れる
    next_rooms = set() #次に進む部屋を探索する
    for nei in neighbors[room]:
      next_rooms.add(nei)
    next_rooms = [room, next_rooms]
    queue.append(next_rooms)
if 0 in lst:
  print('No')
else:
  print('Yes')
  for i in range(n - 1):
    print((lst[i]))

