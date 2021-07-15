from functools import reduce
from math import factorial
n = input()
m = int(''.join((n[0], n[2], n[4], n[3], n[1])))
print('{:0>5d}'.format((m**5)%100000))

