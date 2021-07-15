x,y = map(int,input().split())
L = [list(input()) for _ in range(x)]
F = [['#']*(y+2) for _ in range(x+2)]
for i in range(x):
  for j in range(y):
    F[i+1][j+1] = L[i][j]
for f in F:
  print(''.join(f))
