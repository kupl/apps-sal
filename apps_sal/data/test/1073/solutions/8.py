#!/usr/bin/env python3
n = int(input())
s = input()
ans = 0
for l in range(n-1):
    for r in range(l+1,n+1):
        y, x = 0, 0
        for c in s[l:r]:
            if c == 'U':
                y += 1
            elif c == 'D':
                y -= 1
            elif c == 'R':
                x += 1
            elif c == 'L':
                x -= 1
        if y == 0 and x == 0:
            ans += 1
print(ans)

