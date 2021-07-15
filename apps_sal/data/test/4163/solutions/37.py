num = int(input())
flg_same = False
count = 0

for i in range(num):
  temp = input().split(' ')
  if(temp[0] == temp[1]):
    flg_same = True
  else:
    flg_same = False
    
  if(flg_same):
    count += 1
    if(count == 3):
      break
  else:
    count = 0
if(count == 3):
  print('Yes')
else:
  print('No')

