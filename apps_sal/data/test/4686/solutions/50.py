from collections import Counter as CC
w = list(input())
D = CC(w)
for i in D:
  if D[i] % 2 != 0:
    print('No')
    break
else:
  print('Yes')
