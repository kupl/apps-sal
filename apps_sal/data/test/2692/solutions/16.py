def count(mid,b):
 ans=mid 
 crumb=mid 
 while crumb>=b:
  ans+=crumb//b 
  crumb=crumb//b+crumb%b 
 return ans
for _ in range(int(input())):
 n,b=map(int,input().split())
 low=1 
 high=10**11
 while low<=high:
  mid=(low+high)//2
  if count(mid,b)>=n:
   high=mid-1 
   ans=mid 
  else:
   low=mid+1 
 print(ans)
