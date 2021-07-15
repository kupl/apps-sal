N,C=map(int,input().split())

Dmat=[]
for i in range(C):
  array=list(map(int,input().split()))
  Dmat.append(array)
#print(Dmat)

cmat=[]
for i in range(N):
  array=list(map(int,input().split()))
  cmat.append(array)
#print(cmat)
grid_list=[{},{},{}]
for i in range(N):
  for j in range(N):
    c=cmat[i][j]-1
    mod=(i+j)%3
    if c in grid_list[mod]:
      grid_list[mod][c]+=1
    else:
      grid_list[mod][c]=1
#print(grid_list)

min_cost=10**9
for i in range(C):
  for j in range(C):
    if i==j:
      continue
      
    for k in range(C):
      if i==k or j==k:
        continue
          
      cost=0 
      for c in grid_list[0]:
        num=grid_list[0][c]
        cost+=Dmat[c][i]*num
      for c in grid_list[1]:
        num=grid_list[1][c]
        cost+=Dmat[c][j]*num
      for c in grid_list[2]:
        num=grid_list[2][c]
        cost+=Dmat[c][k]*num
          
      if cost<min_cost:
        #print(i,j,k,cost)
        min_cost=cost
          
print(min_cost)
