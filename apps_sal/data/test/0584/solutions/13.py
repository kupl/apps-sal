import sys
import math
n = int(input())
s = input()
fl = 1
sk = 0
a = [0, 0]
gg = ['(', '_', ')']
i = 0
while i < n:
    if s[i] not in gg:
        y = 0
        while i < n and s[i] not in gg:
            y += 1
            i += 1
        if sk == 0:
            a[0] = max(a[0], y)
        else:
            a[1] += 1
        if i >= n:
            break
    elif s[i] == '(':
        sk = 1
        i += 1
    elif s[i] == ')':
        sk = 0
        i += 1
    else:
        i += 1
print(*a)
