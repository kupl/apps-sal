S = int(input())

flag = [0, 0] # [YYMM, MMYY]
l = S // 100
r = S % 100
if 1<=r and r<=12:
  flag[0] += 1
if 1<=l and l<=12:
  flag[1] += 1
if flag == [0, 0]:
  print('NA')
elif flag == [0, 1]:
  print('MMYY')
elif flag == [1, 0]:
  print('YYMM')
elif flag == [1, 1]:
  print("AMBIGUOUS")
