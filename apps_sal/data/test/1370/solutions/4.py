# coding: utf-8
from itertools import combinations as combs

H,W,K = list(map(int, input().split()))
arr = []
for i in range(H):
  arr.append(list(map(int, list(input()))))

def cut_sum(arr, x1, x2, y):
  ret = 0
  for i in range(x1, x2):
    ret += arr[i][y]
  return ret

row_idxes = list(range(1,H))
min_val = float('inf')

for n_rows in range(H):
  for row_set in combs(row_idxes, n_rows):
    count = len(row_set)
    row_lines = [0] + list(row_set)+ [H]
    col1, col2 = 0, 1
    sums = [0] * (len(row_lines) - 1)
    while col2 <= W:
      row1 = 0
      for box, row2 in enumerate(row_lines[1:]):
        sums[box] += cut_sum(arr, row1, row2, col2-1)
        if sums[box] > K:
          if (col2 - col1) == 1:
            count = float('inf')
            break
          count += 1
          col1 = col2 - 1
          col2 -= 1
          sums = [0] * (len(row_lines) - 1)
          break
        row1 = row2
      if count >= min_val:
        break
      col2 += 1
    
    if min_val > count:
      min_val = count
print(min_val)
