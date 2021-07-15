n=int(input())
a=list(map(int,input().split()))

s=sum(a)

ans=[]

s1=0

for i in range(n):
  if i%2==1:
    s1+=a[i]
    
ans.append(str(s-s1*2))
for j in range(n-1):
  ans.append(str(a[j]*2-int(ans[-1])))
  
print(' '.join(ans))
