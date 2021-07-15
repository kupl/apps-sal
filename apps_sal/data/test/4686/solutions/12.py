s = str(input())
temp = 'a'
flag = 0
for i in range(1,27):
  if s.count(temp)%2==1:
    flag=1
    break
  temp = chr(ord(temp) + 1)
if flag==0:
  print("Yes")
else:
  print("No")
