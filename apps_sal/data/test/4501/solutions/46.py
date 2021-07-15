n,a=map(int,input().split())
from collections import Counter
X = [int(x) - a for x in input().split()]
d=Counter([0])
for i in X:
    tmp=Counter()
    for j,k in d.items():
        tmp[i+j]+=k
    d+=tmp
print(d[0]-1)
