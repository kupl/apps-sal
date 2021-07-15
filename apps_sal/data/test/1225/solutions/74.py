import numpy as np
H=int(input())
c=0
while H!=0:
  c+=1
  H=H//2

print(2**c-1)
