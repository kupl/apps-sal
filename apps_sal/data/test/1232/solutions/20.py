import sys
import os


def getin():
    return list(map(int, input().split(' ')))


(na, nb) = getin()
(k, m) = getin()
a = getin()
b = getin()
if sorted(a)[k - 1] < sorted(b)[nb - m]:
    print('YES')
else:
    print('NO')
