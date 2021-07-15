import numpy as np

l = [list(map(int,input().split())) for i in range(3)]
l_2 =np.array(l).T 

def square(l):
  flag = 1
  for i in range(2):
    for j in range(2):
      if l[j][i] - l[j+1][i] !=  l[j][i+1] - l[j+1][i+1]:
        flag = 0
  return flag
if square(l) * square(l_2) == 1:
  print("Yes")
else:
  print("No")
    








