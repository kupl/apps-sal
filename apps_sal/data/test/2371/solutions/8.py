import sys
readline = sys.stdin.readline

# 最後の一枚を取るか、その直前を取るかしかない
# なぜなら、最後から数えて3枚目を取る場合は相手に最後から2枚目を取ることを期待するが、
# それなら自分が最後から2枚目を取ったほうが有利なため。

N,Z,W = map(int,readline().split())
A = list(map(int,readline().split()))

if N == 1:
  # 1枚の場合は取るしかない
  print(abs(A[0] - W))
  return
  
# 最後の一枚を取る場合
last_one = abs(A[-1] - W)

# 最後から二枚目を取る場合
last_two = abs(A[-1] - A[-2])

if last_one > last_two:
  print(last_one)
else:
  print(last_two)
