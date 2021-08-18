#!/usr/bin/env python

n = int(input())

if n % 2 == 1:
    print((0))
    return

mp = tmp = 0
while True:
    if 5**tmp > n:
        break
    mp = tmp
    tmp += 1

ans = 0
for i in range(1, mp + 1):
    ans += n // (2 * (5**i))

print(ans)
