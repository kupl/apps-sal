n = input()

res = 0
for i in n:
  res += int(i)
  
if int(n)%res == 0:
  print('Yes')
else:
  print('No')
