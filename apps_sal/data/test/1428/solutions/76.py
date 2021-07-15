N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
grid = [list(map(int, input().split())) for _ in range(N)]
D0 = {i: 0 for i in range(C)}
D1 = {i: 0 for i in range(C)}
D2 = {i: 0 for i in range(C)}
for i in range(N):
  for j in range(N):
    if (i+j) % 3 == 0:
      D0[grid[i][j]-1] += 1
    elif (i+j) % 3 == 1:
      D1[grid[i][j]-1] += 1
    elif (i+j) % 3 == 2:
      D2[grid[i][j]-1] += 1
m = int(1e11) + 23
for i in range(C):
  for j in range(C):
    for k in range(C):
      if i != j and j != k and k != i:
        differ = 0
        for l in range(C):
          differ += D0[l] * D[l][i]
          differ += D1[l] * D[l][j]
          differ += D2[l] * D[l][k]
        if m > differ:
          m = differ
print(m)
