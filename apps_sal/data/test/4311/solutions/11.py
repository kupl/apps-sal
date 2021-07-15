s=int(input())
a=[0]*10**6
a[0]=s

def f(x):
  if x%2==0:
    return x//2
  else:
    return 3*x+1
t=0 
while f(a[t])>0:
  p=f(a[t])
  if p in a:
    print((t+2))
    return
  a[t+1]=p
  t+=1

