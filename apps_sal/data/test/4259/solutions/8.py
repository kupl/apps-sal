k = int(input())
a,b = [int(x) for x in input().split()]

flag = 0

for i in range(a, b+1, 1):
    if(i % k == 0):
      flag = 1
      break
    else:
      flag = 0

if(flag):
  print('OK')
else:
  print('NG')
