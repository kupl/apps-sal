def mi():
    return list(map(int, input().split()))
'''
2
2 5
-6 4
7 -2
-1 -3
'''
n = int(input())
c = [0]*n
for i in range(n):
    c[i] = list(mi())
d = [0]*n
for i in range(n):
    d[i] = list(mi())
possans = [0]*(n*n)
k = 0
for i in range(n):
    for j in range(n):
        t1 = (c[i][0]+d[j][0],c[i][1]+d[j][1])
        possans[k] = t1
        k+=1
from collections import Counter
c = Counter(possans)
c = sorted(c, key=c.get)
print(*c[-1])

