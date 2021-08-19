import re
import copy


def accept_input():
    (a, b, c) = list(map(int, input().split()))
    return (a, b, c)


(a, b, c) = accept_input()
aamari = a % b
amaridict = {}
curamari = a % b
for i in range(b):
    curamari = (curamari + aamari) % b
    amaridict[curamari] = 1
if c in amaridict:
    print('YES')
else:
    print('NO')
