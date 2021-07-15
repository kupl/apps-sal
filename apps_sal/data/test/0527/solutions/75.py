from bisect import *
def alph_to_num(s):
  return ord(s)-ord('a')
def solve():
  ans = 0
  S = input()
  T = input()
  lis = [[] for _ in range(26)]
  for i,s in enumerate(S):
    lis[alph_to_num(s)].append(i)
  ind = -1
  for t in T:
    n = alph_to_num(t)
    if not len(lis[n]):
      return -1
    if ind>=lis[n][-1]:
      ans += len(S)
      ind = lis[n][0]
    else:
      ind = lis[n][bisect_right(lis[n],ind)]
  ans += ind+1
  return ans
print(solve())
