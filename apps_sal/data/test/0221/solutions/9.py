s=input().split()
n,k=int(s[0]),int(s[1])
l=2*k+1
m=n%l
if m==0:
    m=2*k+1
if m<=k+1:
    pos=1
else:
    pos=m-k
res=n//l
if n%l!=0:
    res+=1
print(res)
for i in range(res):
    print(pos+l*i,end=" ")
print("")

