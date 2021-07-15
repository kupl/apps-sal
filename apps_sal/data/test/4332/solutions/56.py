a = input()
b = int(a)
sum = 0
for i in a:
  sum += int(i)
if(b%sum == 0):
  print("Yes")
else:
  print("No")
