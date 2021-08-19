import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 9
n = int(input())
r = 'I hate'
for i in range(1, n):
    if i % 2 == 1:
        r += ' that I love'
    else:
        r += ' that I hate'
print(r + ' it')
