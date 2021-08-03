from math import gcd

n = int(input())
a = list(map(int, input().split()))
d = {}
for c in a:
    d[c] = d.get(c, 0) + 1
t = sorted(d)
for x in t:
    if x == 1:
        if d[x] > 1:
            d[x + 1] = d.get(x + 1, 0) + 1
    else:
        if d[x] > 2:
            d[x - 1] = d.get(x - 1, 0) + 1
            d[x + 1] = d.get(x + 1, 0) + 1
        elif d[x] == 2:
            if d.get(x - 1, 0) == 0:
                d[x - 1] = 1
            else:
                d[x + 1] = d.get(x + 1, 0) + 1
        if d[x] == 1 and d.get(x - 1, 0) == 0:
            d[x - 1] = 1
            d[x] = 0

ans = 0
for c in d:
    if d[c]:
        ans += 1
print(ans)
