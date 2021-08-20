import numpy as np
from collections import Counter
n = int(input())
a = np.array(list(map(int, input().split())))
ni = np.array([i for i in range(n)])
ap = a + ni
an = (a - ni) * -1
cp = Counter(ap)
cn = Counter(an)
ans = 0
for i in cp.keys():
    ans += cp[i] * cn[i]
print(ans)
