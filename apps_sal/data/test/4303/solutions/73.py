#!/usr/bin/env python3
n, k, *x = list(map(int, open(0).read().split()))
ans = 10**18
neg = []
pos = [0]
for i in x:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)
neg.append(0)
k += 1
c = len(neg)
c -= k - min(k, len(pos))
k = min(k, len(pos))
while c > 0 and k > 0:
    c -= 1
    k -= 1
    ans = min(ans, -neg[c] * 2 + pos[k], -neg[c] + pos[k] * 2)
print(ans)
