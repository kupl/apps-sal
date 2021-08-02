#!/usr/bin/env python3

a, b = list(map(int, input().split()))

ans = 0
for i in range(1, 13):
    if i < a:
        ans += 1
    elif i == a:
        if i <= b:
            ans += 1
print(ans)
