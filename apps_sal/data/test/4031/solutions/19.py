from math import log
from operator import itemgetter
n = int(input())
si = [[input(), 0] for i in range(n)]
for i in range(n):
    si[i][1] = len(si[i][0])
si.sort(key=itemgetter(1))
ans = 1
for i in range(1, n):
    if si[i - 1][0] not in si[i][0]:
        ans = 0
        break
if ans == 0:
    print('NO')
else:
    print('YES')
    for i in range(n):
        print(si[i][0])
