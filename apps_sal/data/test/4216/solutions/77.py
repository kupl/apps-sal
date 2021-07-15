N=int(input())
res=N
for i in range(1,int(N**(1/2))+1) :
  if N%i==0 :
    res=min(res,N//i)
print(len(str(res)))
