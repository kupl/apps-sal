#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

total = a[0]
xor = a[0]
ans = 0
l = 0
r = 0

while 1:
    if xor == total:
        ans += r-l+1
        r += 1
        if r == n:
            break
        total += a[r]
        xor ^= a[r]
    else:
        total -= a[l]
        xor ^= a[l]
        l += 1
print(ans)

