#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
a.sort()
parent = [a[-1]]
rest = a[:-1]

for _ in range(n):
    next_parent = []
    next_rest = []
    for i in parent[::-1]:
        while(rest):
            x = rest.pop()
            if x < i:
                next_parent.append(x)
                break
            else:
                next_rest.append(x)
                continue
    parent += next_parent
    parent.sort()
    next_rest.reverse()
    rest += next_rest

if len(parent) == 2**n:
    print("Yes")
else:
    print("No")
