
rows, cols = list(map(int, input().split()))

a = [[-1] * cols for _ in range(rows)]

r = list(map(int, input().split()))
c = list(map(int, input().split()))

# print(np.matrix(a))


for row in range(rows):
  for col in range(r[row]):
    a[row][col] = 1
  
  if(r[row] < cols):
    a[row][r[row]] = 0 

# print(np.matrix(a))


for col in range(cols):
  for row in range(c[col]):
    a[row][col] = 1
  
  if(c[col] < rows):
    a[c[col]][col] = 0 

# print(np.matrix(a))

isSol = True

for row in range(rows):
  for col in range(r[row]):
    if a[row][col] != 1 :
      isSol = False

  
  if(r[row] < cols):
    if a[row][r[row]] != 0:
      isSol = False

for col in range(cols):
  for row in range(c[col]):
    if(a[row][col] != 1):
      isSol = False
  
  if(c[col] < rows):
    if (a[c[col]][col] != 0):
      isSol = False

if(isSol):
  sol = 1

  for row in a:
    for i in row:
      if(i == -1):
        sol = (sol * 2) % 1000000007
  
  print(sol)
else:
  print(0)



