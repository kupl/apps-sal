n=int(input())
a=list(map(int,input().split()))
mi=min(a)
cur=0
ans=0
for i in range(3*n):
    if(a[i%n]==mi):
     cur=0
    else:
     cur+=1
    ans=max(ans,cur)
print(n*mi+ans)     
     

