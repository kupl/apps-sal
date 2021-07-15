n,x,y=list(map(int,input().split()))
dic={}
for i in range(1,n+1):
  for j in range(i+1,n+1):
    l=min(j-i,abs(x-i)+1+abs(y-j))
    if l in dic:
      dic[l]+=1
    else:
      dic[l]=1
for l in range(1,n):
  if l in dic:
    print((dic[l]))
  else:
    print((0))

