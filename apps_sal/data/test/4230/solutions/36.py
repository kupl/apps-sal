x,n=map(int,input().split())
if n==0:
  print(x)
  return
p=[int(y) for y in input().split()]
a=0
for i in range(101):
  if x-a not in p:
    print(x-a)
    break
  elif x+a not in p:
    print(x+a)
    break
  a+=1
