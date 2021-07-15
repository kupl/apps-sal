N,A,B=map(int, input().split())
D=[int(input()) for i in range(N)]

def f(a):
  E=[]
  for i in range(N):
    if D[i]-a*B>0:
      E.append(D[i]-a*B)
  cnt=0
  for i in E:
    cnt+=-(-i//(A-B))
  if cnt<=a:
    return True
  else:
    return False
l,r=0,10**9
for i in range(50):
  mid=(l+r)//2
  if f(mid):
    r=mid
  else:
    l=mid
print(r)
