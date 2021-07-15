import numpy as np
h,w = map(int,input().split())
ar = np.array([list(input()) for _ in range(h)]) == '.'
l = np.zeros((h,w),dtype=int)
r = np.zeros((h,w),dtype=int)
u = np.zeros((h,w),dtype=int)
d = np.zeros((h,w),dtype=int)
for i in range(h):
  u[i, :] = (u[i-1]+1)*ar[i]
  d[-i-1, :] = (d[-i]+1)*ar[-i-1]

for j in range(w):
  l[:,j] = (l[:,j-1]+1)*ar[:,j]
  r[:,-j-1] = (r[:,-j]+1)*ar[:,-j-1]
print(np.max(u+d+l+r)-3)
