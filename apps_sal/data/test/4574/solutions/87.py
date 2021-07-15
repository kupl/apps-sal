from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
dd=defaultdict(lambda:0)
for aa in a:
  dd[aa]+=1
x,y=0,0
for k in sorted(dd.keys(), reverse=True):
  if x==0 and dd[k]>=2:
    x=k
    dd[k]-=2
  if y==0 and dd[k]>=2:
    y=k
    break
print(x*y)
