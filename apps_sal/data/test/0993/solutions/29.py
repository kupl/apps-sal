from itertools import accumulate
from collections import defaultdict
N,M=map(int,input().split())
A=list(map(int,input().split()))
acc = [0]+list(accumulate(A,lambda x,y:x+y))
d = defaultdict(list)
for i in range(len(acc)):
    d[acc[i] % M].append(i)
ans = 0
for l in map(len,d.values()):
    ans += l*(l-1)//2
print(ans)
