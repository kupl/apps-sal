import math as mt
import itertools as it
import functools as ft
import random as rnd

stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)

R, x1, y1, x2, y2 = stdin()

if x1 == x2 and y1 == y2:
    print("{} {} {}".format(x1 + (R / 2.), y1, R / 2.))
elif (x2 - x1) ** 2 + (y2 - y1) ** 2 >= R ** 2:
    print('{} {} {}'.format(x1, y1, R))
else:
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    tochka = [x2 + (x1 - x2) * (dist + R) / dist, y2 + (y1 - y2) * (dist + R) / dist]
    print("{} {} {}".format((tochka[0] + x2) / 2, (tochka[1] + y2) / 2, (((tochka[0] - x2) ** 2 + (tochka[1] - y2) ** 2) ** 0.5) / 2))
