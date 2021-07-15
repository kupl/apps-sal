cc = [list(map(int, input().split())) for i in range(3)]
tc = [x for c in cc for x in c]

if sum(tc) % 3 != 0:
  print('No')
else:
  cnt = 0
  for i in range(3):
    cnt  += cc[i][i]
  if cnt == sum(tc)//3:
    print('Yes')
  else:
    print('No')
