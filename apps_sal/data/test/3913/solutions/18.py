
import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/10/22 17:36

"""

N = int(input())
W = input()
M = int(input())

words = set()
for i in range(M):
    words.add(input())

revealed = set(W) - {'*'}
idx = [i for i, w in enumerate(W) if w == '*']
badwords = set()
guesses = set()

for i in idx:
    for u in words:
        if u[i] in revealed:
            badwords.add(u)

for i, w in enumerate(W):
    if w != '*':
        for u in words:
            if u[i] != w:
                badwords.add(u)


words -= badwords

for i in idx:
    w = W[i]
    for u in words:
        c = u[i]
        guesses.add(c)

ans = 0
for g in guesses:
    left = {v for v in words}
    for i in idx:
        for w in {v for v in left}:
            if w[i] == g:
                left.remove(w)
    if not left:
        ans += 1

print(ans)
