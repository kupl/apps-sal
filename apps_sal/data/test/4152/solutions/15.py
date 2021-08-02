from math import *
n = int(input())
a = [int(x) for x in input().split(' ')]
pwrs = [2**i for i in range(1, 31)]
cnts = {}
s = set()
clear = set()
for x in a:
    if x not in cnts:
        cnts[x] = 1
        s.add(x)
    else:
        cnts[x] += 1
for x in cnts:
    for p in pwrs:
        if p - x in s:
            if p - x != x:
                clear.add(x)
                clear.add(p - x)
            elif cnts[x] > 1:
                clear.add(x)
ans = 0
for x in s:
    if x in clear:
        continue
    ans += cnts[x]
print(ans)
