import sys
import os
import fileinput

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a = sorted(a)

i = 0
while k > 0 and i < n:
    if a[i] < 0:
        a[i] = -a[i]
        i += 1
        k -= 1
    else:
        break


if k > 0:
    a = sorted(a)
    if k % 2 != 0:
        a[0] = -a[0]

print(sum(a))
