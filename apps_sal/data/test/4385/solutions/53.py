dis = []
for i in range(5):
  dis.append(int(input()))

k = int(input())

if dis[4] - dis[0] <= k:
  print('Yay!')
else:
  print(':(')

