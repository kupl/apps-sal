N = int (input ())
L1,L2 = 2,1
L3 = 1
x = 1
for i in range (N-1):
  if x == 1:
    L1 = L1+L2
    L3 = L1
    x = 2
  else:
    L2 = L1+L2
    L3 = L2
    x = 1
print (L3)
