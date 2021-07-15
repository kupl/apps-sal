x=input()
x=list(x)
sum=0
for i in x:
  sum+=int(i)
if sum%9==0:
  print("Yes")
else:
  print("No")
