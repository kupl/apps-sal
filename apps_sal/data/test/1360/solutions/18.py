import math
import random
import itertools
import collections
import sys
import time
import fractions
import os
import functools
import bisect


def timer(f):

    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print('Время выполнения функции: %f' % (time.time() - t))
        return res
    return tmp


def contains(l, elem):
    index = bisect.bisect_left(l, elem)
    if index < len(l):
        return l[index] == elem
    return False


n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split(' '))))
array = sorted(array, key=lambda x: x[0] * 100 + x[1])
currentDate = 0
for i in range(len(array)):
    if array[i][0] >= currentDate and array[i][1] >= currentDate:
        currentDate = min(array[i][0], array[i][1])
    elif array[i][0] > currentDate:
        currentDate = array[i][0]
    elif array[i][1] > currentDate:
        currentDate = array[i][1]
print(currentDate)
'\n5\n6 4\n3 2\n3 1\n9 7\n5 3\n'
