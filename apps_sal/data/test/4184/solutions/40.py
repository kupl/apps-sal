a=int(input())
b=list(map(int,input().split()))
c=sum(b)
d=0
e=0
f=0
for i in range(a):
  d=d+b[i]
  if d>=c/2:
    e=i
    break
for i in range(e):
  f=f+b[i]
if abs(d-(c-d))<abs(f-(c-f)):
  print(abs(d-(c-d)))
else:
  print(abs(f-(c-f)))
