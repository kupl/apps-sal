import math
from collections import Counter
from itertools import product


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


a = input()
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
for i in range(len(day)):
    if day[i] == a:
        print(7 - i)
