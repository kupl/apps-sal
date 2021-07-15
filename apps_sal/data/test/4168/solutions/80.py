#!/usr/bin/env python

n = int(input())

if n == 0:
    print((0))
    return

ans = ''
while abs(n) > 0:
    r = n%2 
    ans += str(r) 
    n //= 2
    n = -n

if abs(n)%2 == 1:
    print(ans)
else:
    print((ans[::-1]))

