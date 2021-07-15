#上下左右に#が全て隣接しているならOK

N, M = map(int, input().split())
#print(N)
c = 0
l = []
for i in range(N):
  l.append(list(input()))
  
#print(l)
N -= 1
M -= 1

for i in range(N):
  for j in range(M):
    if l[i][j] == ".":
      pass
    else:
      if i-1>=0 and i+1<=N and j-1>=0 and j+1<=M and l[i-1][j] == "." and l[i+1][j] == "." and l[i][j-1] == "." and l[i][j+1] == ".":
        c+=1
      if i==0 and j-1>=0 and j+1<=M and l[i+1][j] == "." and l[i][j-1] == "." and l[i][j+1] == ".":
        c+=1
      if i-1>=0 and i+1<=N and j==0 and l[i-1][j] == "." and l[i+1][j] == "." and l[i][j+1] == ".":
        c+=1
      if i==N and j-1>=0 and j+1<=M and l[i-1][j] == "." and l[i][j-1] == "." and l[i][j+1] == ".":
        c+=1
      if i-1>=0 and i+1<=N and j-1>=0 and j==M and l[i-1][j] == "." and l[i+1][j] == "." and l[i][j-1] == ".":
        c+=1
      if i==0 and j==0 and l[i+1][j] == "." and l[i][j+1] == ".":
        c+=1
      if i==0 and j==M and l[i+1][j] == "." and l[i][j-1] == ".":
        c+=1
      if i==N and j==0 and l[i-1][j] == "." and l[i][j+1] == ".":
        c+=1
      if i==N and j==M and l[i-1][j] == "." and l[i][j-1] == ".":
        c+=1

if c == 0:
  print("Yes")
else:
  print("No")
