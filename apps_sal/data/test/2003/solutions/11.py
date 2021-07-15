# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/7 22:34

"""


class Node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

N = 32
tree = Node()


def binval(val):
    u = bin(val)[2:]
    return '0' * (N - len(u)) + u


def insert(val):
    u = binval(val)
    t = tree
    for v in u:
        if v == '1':
            if not t.left:
                t.left = Node()
            t = t.left
        else:
            if not t.right:
                t.right = Node()
            t = t.right
    t.val = val


def remove(val):
    u = binval(val)
    t = tree
    q = []
    for v in u:
        nt = t.left if v == '1' else t.right
        q.append((t, v))
        t = nt

    for t, v in reversed(q):
        ended = t.left and t.right
        if v == '1':
            t.left = None
        else:
            t.right = None
        if ended:
            break


def search(val):
    u = binval(((1 << N) - 1) ^ val)
    x = ''
    t = tree
    for v in u:
        if v == '1':
            if t.left:
                x += '1'
                t = t.left
            else:
                x += '0'
                t = t.right
        else:
            if t.right:
                x += '0'
                t = t.right
            else:
                x += '1'
                t = t.left
    return int(x, 2) ^ val


insert(0)
q = int(input())
wc = collections.defaultdict(int)
bwc = collections.defaultdict(set)
ans = []
for qi in range(q):
    a, b = input().split()
    v = int(b)
    if a == '+':
        wc[v] += 1
        if wc[v] == 1:
            insert(v)
    elif a == '-':
        wc[v] -= 1
        if wc[v] == 0:
            remove(v)
    else:
        ans.append(search(v))
print('\n'.join(map(str, ans)))

