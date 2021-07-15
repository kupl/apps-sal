import sys
import numpy as np
input = sys.stdin.readline
h,w = map(int,input().split())
s = (np.array([list(input().strip()) for _ in range(h)])==".").astype(np.int)
l,r,u,d = s.copy(),s.copy(),s.copy(),s.copy()
for i in range(1,w):
  l[:,i] *= l[:,i-1] + 1
  r[:,w-i-1] *= r[:,w-i] + 1

for i in range(1,h):
  u[i] *= u[i-1] + 1
  d[h-i-1] *= d[h-i] + 1
print(max([max(i) for i in l+r+u+d-3]))
