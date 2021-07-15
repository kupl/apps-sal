H, W = map(int,input().split())

mas = [list(map(str,input())) for _ in range(H)]
mas2 = [[0 for _ in range(W+2)] for __ in range(H+2)]

for i in range(1,H+1):
  for j in range(1,W+1):
    if mas[i-1][j-1] == '#':
      mas2[i][j] = -9
      mas2[i+1][j] += 1
      mas2[i+1][j-1] += 1
      mas2[i][j-1] += 1
      mas2[i-1][j-1] += 1
      mas2[i-1][j] += 1
      mas2[i-1][j+1] += 1
      mas2[i][j+1] += 1
      mas2[i+1][j+1] += 1

mas3 = [l[1:-1] for l in mas2[1:-1]]

for k in range(H):
  print(*["#" if i < 0 else i for i in mas3[k]],sep="")
