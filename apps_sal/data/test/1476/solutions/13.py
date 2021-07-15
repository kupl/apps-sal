import sys
from math import *
#sys.stdin = open('inpA.in', 'r')

n = int(input())
a = []
if n > 4:
    for i in range(n - 1, -1, -1):
        if i % 2 == 0:
            a = a + [i + 1]
        else:
            a = [n -i + (n % 2 == 0)] + a
    print(len(a))
    print(' '.join(str(x) for x in a))
elif n == 4:
    print(4)
    print(2, 4, 1, 3)
elif n == 3:
    print(2)
    print(1, 3)
else:
    print(1)
    print(1)

