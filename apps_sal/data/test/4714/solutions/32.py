#!/usr/bin/env python3

a, b = list(map(int, input().split()))

ans = 0
for i in range(a, b + 1):
    i = str(i)
    if i[0] == i[-1] and i[1] == i[-2]:
        ans += 1

print(ans)
