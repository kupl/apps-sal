N=int(input())
n=list(map(int, input().split()))
m=int(sum(n)/N)

def fun(x):
  ans=0
  for i in n:
    ans+=(i-x)**2
  return(ans)
  
p=fun(m)
q=fun(m+1)
if p<q:
  print(p)
else:
  print(q)
