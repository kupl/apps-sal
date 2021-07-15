from sys import stdin
from numpy import argmin

n = int(stdin.readline().strip())
h_lst = [int(x) for x in stdin.readline().split()]
cnt = 0

def glow(lst, start_pos):
  nonlocal cnt
  if len(lst) == 0:
    return -1
  elif len(lst) == 1:
    cnt += lst[0] - start_pos
    return -1
  else:
    pos = min(lst)
    cnt += pos - start_pos
    id_ = argmin(lst)
    glow(lst[:id_], pos)
    glow(lst[id_+1:], pos)
    
glow(h_lst, 0)
print(cnt)

