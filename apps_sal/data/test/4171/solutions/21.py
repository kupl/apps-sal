from collections import *
n, k = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A.sort()
d = defaultdict(lambda: [0, 0])
for i in A:
    num = i
    stp = 0
    while num > 0:
        if d[num][0] < k:
            d[num][0] += 1
            d[num][1] += stp
        num = num // 2
        stp += 1
    if d[num][0] < k:
        d[num][0] += 1
        d[num][1] += stp

mn = 10**20
for i in d:
    if(d[i][0] >= k):
        mn = min(d[i][1], mn)

print(mn)
