n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
ans=""
b=[]
for i in range(n):
 for j in range(i+1,n+1):
  b.append(sum(a[i:j]))
b.sort()
for i in range(k):
 ans+= str(b[len(b)-i-1])+" "
print(ans)
 

