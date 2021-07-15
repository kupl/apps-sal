num=input()
num1=num
j=0
while int(num)>0:
  j+=int(num)%10
  num = int(num)/10
if int(num1)%j==0:
  print("Yes")
else:
  print("No")
