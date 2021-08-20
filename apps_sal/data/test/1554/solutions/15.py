"""
Created on Jan 25, 2016

@author: KANDARP
"""
import sys
n = int(sys.stdin.readline())
arr = [int(x) for x in input().split()]
sets = set()
result = []
ans = 0
l = 0
r = 0
for i in arr:
    if i in sets:
        ans = ans + 1
        sets.clear()
        result.append([l + 1, r + 1])
        l = r + 1
    else:
        sets.add(i)
    r = r + 1
if ans == 0:
    print(-1)
else:
    result[len(result) - 1] = [result[len(result) - 1][0], n]
    print(ans)
    print('\n'.join(('{0} {1}'.format(p, q) for (p, q) in result)))
