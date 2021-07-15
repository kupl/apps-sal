n, m = list(map(int, input().split()))
cl = []
for i in range(n):
  cl.append(input())

def is_squad(x, y):
  if cl[x][y]=='#' and cl[x+1][y]=='#' and cl[x+2][y]=='#' and cl[x+2][y+1]=='#' and cl[x+2][y+2]=='#' and cl[x+1][y+2]=='#' and cl[x][y+2]=='#' and cl[x][y+1]=='#':
    return True
  else:
    return False

def cv(x, y):
  counter = 0
  if x-2>=0 and y+2<=m-1 and is_squad(x-2, y):
    return True
   
  elif x-1>=0 and x+1<=n-1 and y+2<=m-1 and is_squad(x-1, y):
    return True

  elif x+2<=n-1 and y+2<=m-1 and is_squad(x, y):
    return True
  
  elif x+2<=n-1 and y+1<=m-1 and y-1>=0 and is_squad(x, y-1):
    return True

  elif x+2<=n-1 and y-2>=0 and is_squad(x, y-2):
    return True

  elif x+1<=n-1 and x-1>=0 and y-2>=0 and is_squad(x-1, y-2):
    return True

  elif x-2>=0 and y-2>=0 and is_squad(x-2, y-2):
    return True

  elif x-2>=0 and y-1>=0 and y+1<=m-1 and is_squad(x-2, y-1):
    return True
  else:
    return False
  

  

  
  

for i in range(n):
  for j in range(m):
    if cl[i][j]=='#':
      if not cv(i, j):
        print('NO')
        return

print('YES')
