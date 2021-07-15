N, C = map(int, input().split())
d = [list(map(int , input().split())) for _ in range(C)]
c = [list(map(int , input().split())) for _ in range(N)]
#print(d)
#print(c)

from collections import defaultdict
cd = [defaultdict(int), defaultdict(int), defaultdict(int)]
for i in range(N):
    for j in range(N):
        k = (i+1+j+1) % 3
        cd[k][c[i][j]] += 1

ans = 10 ** 10
import itertools
for p in itertools.permutations(list(range(C)), 3):
    iwa = 0
    for ci in cd[0].items():
        iwa += d[ci[0]-1][p[0]] * ci[1]
    for ci in cd[1].items():
        iwa += d[ci[0]-1][p[1]] * ci[1]
    for ci in cd[2].items():
        iwa += d[ci[0]-1][p[2]] * ci[1]
    ans = min(ans, iwa)
#print(cd)
print(ans)
