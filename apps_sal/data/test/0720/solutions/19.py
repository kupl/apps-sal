import math as mt
import itertools as it
import functools as ft
import random as rnd

stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)

n = int(input())

a, b = 0, 0

hap = set()
hap.add(0)
cnt = 1

for i in range(n):
    aa, bb = stdin()
    if max(a, b) <= min(aa, bb):
        cnt += max(-max(a, b) + min(aa, bb) - 1, 0)
        if max(a, b) not in hap:
            cnt += 1
            hap.add(max(a, b))
        if min(aa, bb) not in hap:
            cnt += 1
            hap.add(min(aa, bb))
    a, b = aa, bb

print(cnt)
