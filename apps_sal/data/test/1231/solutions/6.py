#!/usr/bin/env python3
def ri():
    return list(map(int, input().split()))

a, b = ri()

if a == 0 and b == 0:
    print("NO")
    return

diff = abs(a-b)

if diff == 0 or diff == 1:
    print("YES")
else:
    print("NO")

