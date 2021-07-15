N,M = map(int,input().split())
A = list(map(int,input().split()))
cums = [0]
for a in A:
    cums.append(cums[-1] + a)

cump = [c%M for c in cums]
from collections import Counter
ctr = Counter(cump)

ans = 0
for v in ctr.values():
    ans += v*(v-1)//2
print(ans)
