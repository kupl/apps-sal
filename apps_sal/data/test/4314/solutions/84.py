h, w = map(int, input().split())
grid = []
for _ in range(h):
  grid.append(list(input()))
  
delete_row = []
for i in range(h):
  for j in range(w):
    if grid[i][j] != '.':
      break
    elif j == w-1:
      delete_row.append(i)
      
delete_col = []
for j in range(w):
  for i in range(h):
    if grid[i][j] != '.':
      break
    elif i == h-1:
      delete_col.append(j)
      
for i in range(h):
  if i not in delete_row:
    for j in range(w):
      if j not in delete_col:
        print(grid[i][j], end='')
    print()

