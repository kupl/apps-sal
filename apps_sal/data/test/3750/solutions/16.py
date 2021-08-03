#!/usr/bin/env python3
k, a, b = [int(x) for x in input().strip().split()]
qa = a // k
qb = b // k
a %= k
b %= k

if qa == 0 and b != 0:
    print(-1)
elif qb == 0 and a != 0:
    print(-1)
else:
    print(qa + qb)
