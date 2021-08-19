from sys import stdin, stdout
import math
from collections import defaultdict
# from collections import OrderedDict
from collections import Counter
# from queue import deque
# from math import log2


def arrinp():
    return [*list(map(int, stdin.readline().split(' ')))]


def mulinp():
    return list(map(int, stdin.readline().split(' ')))


def intinp():
    return int(stdin.readline())


def inp():
    return stdin.readline()


def solution():
    n = intinp()
    if n > 30:
        if n - 30 == 6:
            print('YES')
            print(5, 6, 10, 15)
        elif n - 30 == 10:
            print('YES')
            print(6, 10, 15, 9)
        elif n - 30 == 14:
            print('YES')
            print(6, 10, 15, 13)
        else:
            print('YES')
            print(6, 10, 14, n - 30)
    else:
        print('NO')


testcases = 1
testcases = intinp()
for _ in range(testcases):
    solution()
