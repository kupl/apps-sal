a=input()
b=""
for i in range(1,len(a)+1):
  b+=a[-i]
if a==b:
  print("Yes")
else:
  print("No")
