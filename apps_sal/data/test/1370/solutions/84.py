from itertools import *

H, W, K = list(map(int, input().split()))
S = [list(map(int, input())) for i in range(H)]

cut_min = H+W-2

for r_cut in range(H):
  if cut_min <= r_cut:
    continue
  for r_pos in combinations(list(range(1, H)), r_cut):
    r_pos = (None,)+r_pos+(None,)
    r_blocks = [slice(*r_pos[i:i+2]) for i in range(len(r_pos)-1)]
    
    cut = r_cut
    prev_sum = [0] * len(r_blocks)
    for col in zip(*S):
      curr_sum = [sum(col[b]) for b in r_blocks]
      if any(map(K.__lt__, curr_sum)):
        break
      next_sum = [x+y for x,y in zip(prev_sum, curr_sum)]
      if any(map(K.__lt__, next_sum)):
        cut += 1
        if cut_min <= cut:
          break
        prev_sum = curr_sum
      else:
        prev_sum = next_sum
    else:
      cut_min = cut
print(cut_min)

