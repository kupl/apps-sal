#袋を置き終わって排他的論理和が0の時負け、0じゃない時勝ち
#Nが偶数なら先手は0にならないようにする。後手は0にする。
#先手がいかに頑張っても後手が0にできるなら、後手の勝ち
#それ以外は先手の勝ち
#Nが奇数なら逆

import collections
def game(n, A):#計算量log以下が求められる。
  #先手番
  if N % 2 == 0:
    ans = "Second"
    B = collections.Counter(A)
    for i in list(B.values()):
      if i % 2 != 0:
        ans = "First"
  #後手番  
  else:
    ans = "Second"
  return ans

T = int(input())
for i in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  score = game(N, A)
  print(score)

