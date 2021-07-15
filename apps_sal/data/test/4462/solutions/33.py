n = int(input())
a_lst = list(map(int, input().split()))

cnt = 0
for a in a_lst:
  if a % 4 == 0:
    cnt += 2
  elif a % 2 == 0:
    cnt += 1
  else:
    pass

if cnt // 2 >= n // 2:
  print('Yes')
else:
  print('No')
