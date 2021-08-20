from math import *
lst = input().split()
if sqrt(int(lst[0] + lst[1])) % 1 == 0:
    print('Yes')
else:
    print('No')
