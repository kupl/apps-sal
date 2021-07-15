n = int(input())
a = list(map(int,input().split()))
max_num = a[0]
if n==1:
  print('Yes')
  
else:
  flag = True
  for i in range(1,n):
    max_num = max(max_num,a[i])
    if max_num-a[i]>=2:
      print('No')
      flag = False
      break
    else:
      pass
  if flag == True:
    print('Yes')
