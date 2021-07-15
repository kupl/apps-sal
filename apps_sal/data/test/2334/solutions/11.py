import math
n=int(input())
a=list(map(int,input().split()))
x,f=map(int,input().split())
t=x+f
ans=0
for i in a:
  if(i>x):
    ans+=int(math.ceil(((i-x)/t)))
print(ans*f)
