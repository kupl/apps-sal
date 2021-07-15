n, m, x = map(int, input().split())
inp=[]

# 入力をすべて受け取る
for i in range(n):
  tmp = list(map(int, input().split()))
  inp.append(tmp)

# bit全探索を行うための箱づくり
sum = 0
min = 10**10
for i in range(2**n):
  tmp = [0]*m
  flg = 0
  
  # ある買う買わないのケースに対して、フラグが立ってたらスキルポイントを増やす
  for j in range(n):
    if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
      sum += inp[j][0]
      for k in range(1,m+1):
        #print(n,j, k, tmp, inp)
        tmp[k-1] += inp[j][k]
  for ii, k in enumerate(tmp):
    if k < x: # x未満ならflgをたててNGとする
      flg = 1
      break
  #print(tmp, flg)
  if sum < min and flg == 0: min = sum
  sum = 0
  
if min == 10**10: min = -1
print(min)
