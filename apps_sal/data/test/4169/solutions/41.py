N,M = map(int,input().split())
AB = []
money = 0
drinks = 0

for i in range(N):
  A,B = map(int,input().split())
  AB.append([A,B])

AB.sort()

for i in range(N):
  if 0 < M-drinks < AB[i][1]:
    money += (M-drinks)*AB[i][0]
    break
  elif AB[i][1] <= M-drinks:
    money += AB[i][1]*AB[i][0]
    drinks += AB[i][1]
  else:
    break
    
print(money)
