w = input()

import collections as c

counts = c.Counter(w)
if all(elem % 2 == 0 for elem in counts.values()):
  print('Yes')
else:
  print('No')
