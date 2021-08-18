# import getpass
# import math
# import sys
# import string
# import re
# import math
# import random
# from decimal import Decimal, getcontext


def ria():
    return [int(i) for i in input().split()]


# if getpass.getuser() != 'frohenk':
#     filename = 'half'
#     # sys.stdin = open('input.txt')
#     # sys.stdout = open('output.txt', 'w')
# else:
#     sys.stdin = open('input.txt')
#     # sys.stdin.close()

h, w = ria()

mt1 = []
mt2 = []

for y in range(h):
    mt1.append(ria())
for y in range(h):
    mt2.append(ria())
# now its y then x

# print(mt1, mt2)

for x in range(w):
    st1 = []
    st2 = []

    y = 0
    while w > x >= 0 and h > y >= 0:
        st1.append(mt1[y][x])
        st2.append(mt2[y][x])
        x -= 1
        y += 1

    st1.sort()
    st2.sort()
    if st1 != st2:
        print('NO')
        return

for y in range(h):
    st1 = []
    st2 = []

    x = w - 1
    while w > x >= 0 and h > y >= 0:
        st1.append(mt1[y][x])
        st2.append(mt2[y][x])
        x -= 1
        y += 1
    # print(st1)
    # print(st2)
    #
    st1.sort()
    st2.sort()
    if st1 != st2:
        print('NO')
        return
print('YES')
