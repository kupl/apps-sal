cnt = 0
M = int(input())
for i in range(M):
  x, y = map(int, input().split())
  if x == y :
    cnt += 1
  else:
    cnt = 0
  if cnt == 3:
    print('Yes')
    break
if cnt < 3:
  print('No')
