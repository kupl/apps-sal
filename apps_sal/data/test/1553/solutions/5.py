n,h=map(int,input().split())
l=list(map(int,input().split()))
ans=0
for i in range(n):
         curr=0
         ls=sorted(l[:i+1])
         for j in range(i,-1,-2):
                  curr+=ls[j]
         if(curr>h):
                  break
         else:
                  ans=i
print(ans+1)
