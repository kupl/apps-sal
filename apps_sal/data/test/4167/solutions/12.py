n,k=list(map(int,input().split()))
am_0=[]
am_k2=[]

if k%2==0:
  for i in range(1,n+1):
    if i%k==0:
      am_0.append(i)
    
    elif i%k==(k//2):
      am_k2.append(i)
  print((len(am_0)**3+len(am_k2)**3))
  
else:
  print((pow((n//k),3)))

