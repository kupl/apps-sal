#!/usr/bin/env python3
S = input()
ans = 0
for s in S:
    if s =='+':
        ans += 1
    else:
        ans -= 1
print(ans)
