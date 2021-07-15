#!/usr/bin/env python3
n, k, *x = list(map(int, open(0).read().split()))
ans = 10**18
neg = [i for i in x if i<0]+[0]
pos = [0]+[i for i in x if i>=0]
l = len(neg) -max(0, k + 1 - len(pos))
r = min(k+1, len(pos))
while l > 0 and r > 0:
    l -= 1
    r -= 1
    ans = min(ans, -neg[l] * 2 + pos[r], -neg[l] + pos[r] * 2)
print(ans)

