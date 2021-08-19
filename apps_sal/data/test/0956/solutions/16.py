from collections import defaultdict
import sys
#sys.stdin = open('inp.txt', 'r')

m, k = map(int, input().split())
a, a2 = defaultdict(list), defaultdict(list)
for i in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
for x in a:
    for y in a:
        tmp = 0
        if x != y and y not in a[x]:
            tmp += len(set(a[x]) & set(a[y]))
            if tmp / (len(a[x]) / 100.0) >= k:
                a2[x].append(y)
ans = []
for x in a:
    if x in a2:
        ans += [[x, sorted([y for y in a2[x]])]]
    else:
        ans += [[x, []]]
ans.sort()
for x in ans:
    print(str(x[0]) + ':', len(x[1]), ' '.join(str(z) for z in (y for y in x[1])))
