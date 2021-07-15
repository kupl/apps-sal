from functools import reduce
from operator import mul

def solve():
  N = int(input())
  S = input()
  RGB_count = {'R':0,'G':0,'B':0} # R,G,B
  RGB_set = {'R','G','B'}
  ret = 0
  for s in S:
    ret += reduce(mul, [RGB_count[t] for t in RGB_set - {s}])
    RGB_count[s] = RGB_count[s] + 1

  # print(ret)
  RGB_mergin_len = 0
  # R.{l}G.{l}B
  while 3+RGB_mergin_len*2 <= N:
    for i in range(N-(3+RGB_mergin_len*2)+1):
      j = i+1+RGB_mergin_len
      k = i+2+2*RGB_mergin_len
      if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
        ret -= 1

      # print(i, j, k)
      # print(S[i], S[j], S[k], ret)
    RGB_mergin_len += 1

  print(ret)
  
solve()
