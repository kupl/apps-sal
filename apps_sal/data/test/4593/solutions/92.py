a=int(input())
d=0
e=0
for i in range(40):
  b=i+2
  while b<=a:
    b=b*(i+2)
    e=e+1
  c=b/(i+2)
  if e>1:
    if d<=c:
      d=c
      e=0
  else:
    e=0
if d==0:
  print(1)
else:
  print(int(d))
