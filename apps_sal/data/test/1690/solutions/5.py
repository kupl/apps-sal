n=int(input())
l=list(map(int,input().split()))
ans=0
curr=1000000001
for i in range(n-1,-1,-1):
         if(l[i]<curr):
                  curr=l[i]
         elif(curr>0):
                  curr-=1
         ans+=curr
print(ans)
