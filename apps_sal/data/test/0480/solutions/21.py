s,x1,x2 = [int(i) for i in input().strip().split()]
t1,t2 = [int(i) for i in input().strip().split()]
p,d = [int(i) for i in input().strip().split()]

d2 = 1 if x2-x1>0 else -1
ans = abs(x2-x1)*t2

if d==d2==1:
  if p<=x1:
    ans = min(ans,(x2-p)*t1)
  elif p>x1:
    ans = min(ans,(2*s-p+x2)*t1)
elif d==d2==-1:
  if p>=x1:
    ans = min(ans,(p-x2)*t1)
  elif p<x1:
    ans = min(ans,(2*s+p-x2)*t1)
elif d!=d2 and d==1:
  ans = min(ans,(2*s-p-x2)*t1)
elif d!=d2 and d==-1:
  ans = min(ans,(p+x2)*t1)

print(ans)
