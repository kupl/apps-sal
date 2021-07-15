n = int(input())
if n==0:
  print(0)
  return
if n==1:
  print(1)
  return
l = []
while n!=1:
  if n%2==0:
    n //= -2
    l.append(0)
  else:
    n = (n-1)//(-2)
    l.append(1)
l.append(1)
l = l[::-1]
print(*l,sep="")
