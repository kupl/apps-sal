import re
import math
import decimal
import bisect


def read():
    return input().strip()


def iread():
    return int(input().strip())


def viread():
    return [int(x) for x in input().strip().split()]


line = read()
can = False
for i in range(len(line) - 2):
    check = line[i:i + 3]
    if 'B' in check and 'A' in check and ('C' in check):
        can = True
        break
print('Yes' if can else 'No')
