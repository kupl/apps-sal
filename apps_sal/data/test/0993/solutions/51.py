n,m = map(int, input().split())
al = list(map(int, input().split())) 

res = 0

def c(x):
    y = x*(x-1)//2
    return y

import itertools
als= list(itertools.accumulate(al))

alm = list(map(lambda x:x %m,als))

from collections import Counter
count = Counter(alm)
for i in count:
    if count[i]>1:
        res += c(count[i])

res += count[0]
print(res)
