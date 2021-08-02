__author__ = 'Utena'
from functools import cmp_to_key
n = int(input())
s = []
for i in range(n):
    s.append(input())


def cmp(x, y):
    if x + y < y + x:
        return -1
    else:
        return 1


s = sorted(s, key=cmp_to_key(cmp))
print(''.join(s))
