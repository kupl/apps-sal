H, W = list(map(int, input().split()))
grid = []

for _ in range(H):
  grid.append([s for s in input()])

for i in range(H):
  for j in range(W):
    r_ij = grid[i][j]
    if r_ij == "#":
      continue
    c_ij = 0
    if 1<=i<=H-1 and 1<=j<=W-1:
      if grid[i-1][j-1] == "#":
        c_ij += 1
    if 1<=i<=H-1 and 0<=j<=W-1:
      if grid[i-1][j] == "#":
        c_ij += 1
    if 1<=i<=H-1 and 0<=j<=W-2:
      if grid[i-1][j+1] == "#":
        c_ij += 1
    if 0<=i<=H-1 and 1<=j<=W-1:
      if grid[i][j-1] == "#":
        c_ij += 1
    if 0<=i<=H-1 and 0<=j<=W-2:
      if grid[i][j+1] == "#":
        c_ij += 1
    if 0<=i<=H-2 and 1<=j<=W-1:
      if grid[i+1][j-1] == "#":
        c_ij += 1
    if 0<=i<=H-2 and 0<=j<=W-1:
      if grid[i+1][j] == "#":
        c_ij += 1
    if 0<=i<=H-2 and 0<=j<=W-2:
      if grid[i+1][j+1] == "#":
        c_ij += 1
    grid[i][j] = str(c_ij)

str_list = ["".join(s) for s in grid]
for s in str_list:
  print(s)

