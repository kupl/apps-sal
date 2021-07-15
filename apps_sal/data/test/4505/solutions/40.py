import numpy as np

S=input()

s = [st for st in S]
if len(np.unique(s)) == 3:
  print("Yes")
else:
  print("No")
