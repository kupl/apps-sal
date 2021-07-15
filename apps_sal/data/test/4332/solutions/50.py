a=input()
b=0
for i in range(len(a)):
  b=b+int(a[i])
if (int(a)%b==0):
  print("Yes")
else:
  print("No")
