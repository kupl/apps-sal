import numpy as np
S = list(input())
n = len(S)
ans = [0] * n
right_flag = False
for i, s in enumerate(S):
  if s == 'R' and right_flag is False:
    right_index = i
    right_flag = True
  elif s == 'L' and right_flag:
    right_flag = False
    cnt = i - right_index
    odd = cnt // 2
    even = cnt - odd
    ans[i-1] += even
    ans[i] += odd
left_flag = False
for i, s in enumerate(S[::-1], 1):
  if s == 'L' and left_flag is False:
    left_index = i
    left_flag = True
  elif s == 'R' and left_flag:
    left_flag = False
    cnt = i - left_index
    odd = cnt // 2
    even = cnt - odd
    ans[-i+1] += even
    ans[-i] += odd
print(*ans)
