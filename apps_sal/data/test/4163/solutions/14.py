n = int(input())
cnt = 0
for i in range(n):
  d1, d2 = list(map(int, input().split()))
  if d1 == d2:
    cnt += 1
  else:
    cnt = 0
  if cnt >= 3:
    break
if cnt >= 3:
  print('Yes')
else:
  print('No')
