import math as mt
import itertools as it
import functools as ft
import random as rnd
stdin = lambda type_='int', sep=' ': list(map(eval(type_), input().split(sep)))
joint = lambda sep=' ', *args: sep.join((str(i) if type(i) != list else sep.join(map(str, i)) for i in args))
(w1, h1, w2, h2) = stdin()
print(2 * (h1 + h2) + w1 + w2 + 4 + max(w1 - w2, 0))
