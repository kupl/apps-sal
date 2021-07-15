from collections import defaultdict
from queue import deque


def arrinp():
    return [*list(map(int, input().split(' ')))]


def mulinp():
    return list(map(int, input().split(' ')))


def intinp():
    return int(input())


def solution():
    n = intinp()
    s = input()
    if n%2 == 0:
        win = 1
        for i in range(n):
            if i%2 == 1:
                if int(s[i])%2 == 0:
                    win = 2
    else:
        win = 2
        for i in range(n):
            if i%2 == 0:
                if int(s[i])%2 == 1:
                    win = 1
    print(win)
    return


testcases = 1
testcases = int(input())
for _ in range(testcases):
    solution()

