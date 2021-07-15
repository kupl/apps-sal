N = int(input())
cnt = 0
for i in range(N):
  a,b = map(int, input().split())
  if a == b:
    cnt+=1
  elif cnt == 3:
    break
  else:
    cnt = 0
if cnt >= 3:
  print('Yes')
else:
  print('No')
