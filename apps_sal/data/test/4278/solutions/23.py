from collections import defaultdict

n=int(input())
l=[]
clst=defaultdict(lambda:0)
for i in range(n):
  clst[str(sorted(input()))]+=1
  
ans=0
for x in clst.values():
  x-=1
  if x > 0:
    ans+=(1+x)*x//2 
print(ans)
