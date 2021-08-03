from collections import defaultdict
n, s = int(input()), []
for i in range(n):
    a = [int(x) for x in input().split()]
    s += [(a[0], 0), (a[1], 1)]
s.sort()
now, rev = 0, defaultdict(int)
for a, b in zip(s, s[1:]):
    now += 1 if a[1] == 0 else -1
    if(a[1] == 0):
        rev[now] += b[0] - a[0] + (1 if b[1] == 1 else 0)
    elif b[0] != a[0]:
        rev[now] += b[0] - a[0] - (1 if b[1] == 0 else 0)
[print(rev[i], end=" ") for i in range(1, n + 1)]
