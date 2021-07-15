X=list(map(int,input().split()))
X.sort()
ans=X[2]-X[1]
if (X[2]-(X[0]+ans))%2==0:
  print(ans+(X[2]-(X[0]+ans))//2)
else:
  print(ans+(X[2]-(X[0]+ans)+1)//2+1)
