import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
'\ncreated by shhuan at 2018/10/20 22:37\n\n'
'\n# Definition for a Node.\n'
N = int(input())
A = [int(x) for x in input().split()]
e = 2 * sum(A)
ans = max(e // N + 1, max(A))
print(ans)
