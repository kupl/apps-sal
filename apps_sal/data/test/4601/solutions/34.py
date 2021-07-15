n,k = list(map(int,input().split()))
enemy = list(map(int,input().split()))

enemy.sort(reverse=True)

if k >= n :
  print((0))

else:
  

  for x in range(k):
    enemy[x] = 0
  
  print((sum(enemy)))

