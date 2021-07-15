from sys import stdin, stdout

# from collections import defaultdict
# from collections import OrderedDict
# from collections import Counter
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
    l, r = mulinp()
    if r < 2*l:
        print(-1, -1)
        return
    else:
        print(l, 2*l)
        return


testcases = 1
testcases = intinp()
for _ in range(testcases):
    solution()

