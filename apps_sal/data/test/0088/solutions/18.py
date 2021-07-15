#!/bin/python
import collections
import random
import sys
try:
    from tqdm import tqdm
except:
    def tqdm(iterable):
        return iterable


__taskname = ''
if __taskname:
    sys.stdin = open(__taskname + '.in')
    sys.stdout = open(__taskname + '.out', 'w')

def f(n):
    result = set()
    i = 0
    while (1 << i) <= 4 * n:
        for j in range(i - 1):
            if (1 << i) - 1 - (1 << j) <= n:
                result.add((1 << i) - 1 - (1 << j))
        i += 1
    return len(result)


a, b = list(map(int, input().split()))
print(f(b) - f(a - 1))

