N,MA,MB = map(int,input().split())
ABC = [tuple(map(int,input().split())) for i in range(N)]

from collections import defaultdict
from copy import copy
d = defaultdict(lambda: float('inf'))
d[(0,0)] = 0
for a,b,c in ABC:
    d2 = copy(d)
    for (pa,pb),pc in d.items():
        d2[(pa+a, pb+b)] = min(d2[(pa+a, pb+b)], pc+c)
    d = d2

ans = float('inf')
for (a,b),c in d.items():
    if a==b==0: continue
    if a*MB == b*MA:
        ans = min(ans, c)
print(-1 if ans==float('inf') else ans)
