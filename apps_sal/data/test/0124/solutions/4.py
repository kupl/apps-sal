import math as mt
import itertools as it
import functools as ft
import random as rnd

stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)

x, y, z = stdin()
a, b, c = stdin()

a -= x

if a < 0:
    print("NO")
    return

if a + b < y:
    print("NO")
    return

if a + b + c < y + z:
    print("NO")
    return

print("YES")
