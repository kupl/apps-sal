a=input()
b=int(a)
s=0
for i in range(len(a)):
  s=s+int(a[i])
if b%s==0:
  print("Yes")
else:
  print("No")
