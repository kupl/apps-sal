# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/9 23:05

"""

N = int(input())
S = input()


u, d, l, r = S.count('U'), S.count('D'), S.count('L'), S.count('R')

print(N - abs(u-d) - abs(l-r))
