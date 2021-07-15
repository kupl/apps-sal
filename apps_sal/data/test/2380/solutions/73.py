n,m=map(int,input().split())
A=sorted(list(map(int,input().split())))
BC=[list(map(int,input().split())) for i in range(m)]
BC=sorted(BC,reverse=True,key=lambda x: x[1])
flag=0
t=0
for i in range(m):
  if flag==1:
    break
  for j in range(t,n):
    if BC[i][1]>A[j]:
      A[j]=BC[i][1]
      BC[i][0]-=1
      t=j+1
      if BC[i][0]==0:
        break
    else:
      flag=1
      break
print(sum(A))
