from math import *
from itertools import *
from collections import *
from functools import reduce


def input_ints():
    return list(map(int, input().split()))


def input_floats():
    return list(map(float, input().split()))


def input_strings():
    return input().split()


n = int(input())

a = ceil(sqrt(n))
b = ceil(n / a)

print(a + b)
