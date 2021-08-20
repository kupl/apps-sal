import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
'\ncreated by shhuan at 2017/11/9 23:05\n\n'
N = int(input())
S = input()
(u, d, l, r) = (S.count('U'), S.count('D'), S.count('L'), S.count('R'))
print(N - abs(u - d) - abs(l - r))
