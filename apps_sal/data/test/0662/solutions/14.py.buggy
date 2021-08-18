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
created by shhuan at 2017/11/23 23:06

"""

N = int(input())


players = {1, 2}

for i in range(N):
    a = int(input())
    if a not in players:
        print("NO")
        return

    np = {1, 2, 3} - players

    players = np | {a}

print("YES")
