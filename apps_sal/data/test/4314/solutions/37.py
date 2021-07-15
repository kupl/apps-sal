import numpy as np
h,w=map(int, input().split())
a=[list(input()) for i in range(h)]
a=np.array(a)

a2=[]
a3=[]
for i in range(h):
  if "#" in a[i]:
    a2.append(a[i])
a2=np.array(a2)
a2=a2.T

for i in range(len(a2)):
  if "#" in a2[i]:
    a3.append(a2[i])
a3=np.array(a3)
a3=a3.T
for i in range(len(a3)):
  print("".join(a3[i]))
