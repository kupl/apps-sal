#!/usr/bin/env python

n = int(input())

if n == 0:
    print((0))
    return

ans = ''
while abs(n) > 0:
    r = n%2 
    ans = str(r) + ans 
    
    if r == 1:
        n -= 1
    n //= (-2)

print(ans)

