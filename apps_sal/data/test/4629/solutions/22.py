a = [0,1,2,3,4,5,6,7,8,9]
from itertools import combinations
import bisect
c = []
for i in range(1,10):
    c+=list(combinations(a,i))
p = set()
for i in range(len(c)):
    l = 0
    for j in range(len(c[i])):
        l+=pow(3,c[i][j])
    p.add(l)
p = list(p)
p = sorted(p)
q = int(input())
for _ in range(q):
    n = int(input())
    k = bisect.bisect_left(p,n)
    if p[k]==n:
        print(n)
    else:
        print(p[k])
