import itertools
import numpy as np

bit_base = 2#bit_base^nの全探査になる. 
def Base_10_to_n(X, n):#10進数をbit_base進数に変換
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out

def main():
  N, M = list(map(int, input().split()))
  cake = []
  for i in range(N):
    cake.append(list(map(int, input().split())))
  cake = np.array(cake)
  ans = 0
  n = 3
  for i in range(bit_base**n):
    s = Base_10_to_n(i, bit_base)
    s = s.zfill(n)
    cake_temp = cake.copy()
    for num, j in enumerate(s):
      if j == '0':
        cake_temp[:, num] *= -1
    cake_temp = np.sum(cake_temp, axis = 1)
    cake_temp = sorted(cake_temp)
    ans = max(sum(cake_temp[-M:]), ans)
  if M == 0:
    ans = 0
  print(ans)
  
def __starting_point():
  main()

__starting_point()
