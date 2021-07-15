k,q = input().split()
k = int(k)
q = int(q)

d = input().split()
for i in range(k):
    d[i] = int(d[i]) - 1

import numpy as np
d = np.array(d)

for r in range(q):
    n,x,m = input().split()
    n = int(n)
    x = int(x)
    m = int(m)

    dd = d % m + np.ones(k,dtype="int")
    DD = np.concatenate((np.zeros(1, dtype="int"),np.cumsum(dd) ))
    
    alast = x + DD[k]*((n-1)//k) + DD[(n-1)%k]
    kuriagari = alast // m - x//m

#    print([x%m, alast, alast%m, n - kuriagari - 1])
    print (n - 1 - kuriagari)
