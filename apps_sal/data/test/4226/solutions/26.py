X,Y=map(int,input().split())
num=0
for a in range(X+1):
  if 2*a+4*(X-a)==Y:
    num=num+1
if num>=1:
  print("Yes")
else:
  print("No")
