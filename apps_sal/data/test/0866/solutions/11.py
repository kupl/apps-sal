mod=10**9+7

x,y=map(int,input().split())
if (x+y)%3!=0:
  print(0)
  return
  
if x*2<y or y*2<x:
  print(0)
  return
  
z=(x+y)//3

x-=z
y-=z

n=x+y
r=x

if x==0 or y==0:
  print(1)
  return
  

lst=[0]+[1]
for i in range(2,n+10):
  lst.append((lst[-1]*i)%mod)


xxx=lst[n]
xxx*=pow(lst[n-r],10**9+5,mod)
xxx%=mod
xxx*=pow(lst[r],10**9+5,mod)
xxx%=mod

print(xxx)
