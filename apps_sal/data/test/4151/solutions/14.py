from collections import defaultdict
n = int(input())
a = [int(x) for x in input().split()]
d = defaultdict(list)
for i in range(n):
    if a[i] not in d:
        d[a[i]] = [i, i]
    d[a[i]][1] = i

cmax = 0
num = -1
for i in range(n):
    if d[a[i]][1] > cmax:
        cmax = d[a[i]][1]
    if cmax == i:
        num += 1
print(pow(2, num, 998244353))
