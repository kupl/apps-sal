w,h,n=map(int,input().split())
s=0
b=w
t=0
c=h

for i in range(n):
  x,y,a=map(int,input().split())
  if a==1:
    s=max(s,x)
  elif a==2:
    b=min(b,x)
  elif a==3:
    t=max(t,y)
  else:
    c=min(c,y)
if b>s and c>t:
   print((b-s)*(c-t))
else:
  print(0)
