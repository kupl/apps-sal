k,x=map(int,input().split())
maxk=x+k-1
mink=x-k+1
l=[]
for i in range(mink,maxk+1):
  l.append(str(i))
print(" ".join(l))
