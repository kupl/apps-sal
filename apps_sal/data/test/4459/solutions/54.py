import math
from collections import Counter
from itertools import product

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n = ii()
a = li()

cnt = Counter(a)
ans = 0
for i,j in cnt.items():
    if i > j:
        ans += j
    else:
        ans += j - i
print(ans)
