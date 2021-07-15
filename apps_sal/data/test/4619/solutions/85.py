W, H, N = list(map(int, input().split()))
input_list = []
for i in range(N):
  input_list.append(list(map(int, input().split())))

point_list = []
for h in range(H):
  list_ = []
  for w in range(W):
    list_.append(1)
  point_list.append(list_)

for input_ in input_list:
  x, y, a = input_
  if a == 1:
    for h in range(H):
      for i in range(x):
        point_list[h][i] = 0
  if a == 2:
    for h in range(H):
      for i in range(x, W):
        point_list[h][i] = 0
  if a == 3:
    for i in range(y):
      for w in range(W):
        point_list[i][w] = 0
  if a == 4:
    for i in range(y, H):
      for w in range(W):
        point_list[i][w] = 0

ans = sum([sum(point) for point in point_list])
print(ans)

