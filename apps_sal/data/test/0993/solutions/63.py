n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
d={0:1}
s=0
for i in a:
  s=(s+i)%m
  if s in d:
    d[s]+=1
  else:
    d[s]=1
    
def f(x):
  return int(x*(x-1)/2)

s=0
for i in d:
  s+=f(d[i])
print(s)
