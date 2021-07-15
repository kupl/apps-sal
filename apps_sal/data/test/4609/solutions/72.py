import collections
import numpy as np
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
ans = collections.Counter(a)
c=list(ans.values())
c=np.array(c)
print(sum(c%2))
