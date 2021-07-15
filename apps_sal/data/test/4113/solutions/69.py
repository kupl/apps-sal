a=int(input())
b=0
for i in range(26):
  for h in range(15):
    if i*4+h*7==a:
      b=b+1
if b==0:
  print("No")
else:
  print("Yes")
