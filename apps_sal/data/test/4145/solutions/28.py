x = int(input())
num=2
while num<x:
  if x%num==0:
    x+=1
    num=2
  else:
    num+=1
print(x)
