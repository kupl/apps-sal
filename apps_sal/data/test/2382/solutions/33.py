#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
a.sort()
parent = [a[-1]]
rest = a[:-1]
for _ in range(n):
    next_parent = []
    next_rest = []
    for p in parent[::-1]:
        while rest:
            x = rest.pop()
            if x < p:
                next_parent.append(x)
                break
            else:
                next_rest.append(x)
                continue
    parent += next_parent
    parent.sort()
    rest = rest + next_rest[::-1]

if len(parent) == 2**n:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
