a = list(input())
sum = 0
n = ""
for i in range(len(a)):
  n += a[i]
  sum += int(a[i])
if int(n)%sum == 0:
  print("Yes")
else:
  print("No")
