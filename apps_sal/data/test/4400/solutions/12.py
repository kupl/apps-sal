str = input()

#直前の文字が雨か判定するフラグ
flg = False
#連続count数
count = 0
#最大count数
max = 0

for s in str:
  if s == 'R':
    if flg == True:
      count += 1
      if max < count:
        max = count
    else:
      flg = True
      count += 1
      if max < count:
        max = count
  else:
    flg = False
    count = 0

print(max)

