from collections import defaultdict
from queue import deque


def arrinp():
    return [*list(map(int, input().split(' ')))]


def mulinp():
    return list(map(int, input().split(' ')))


def intinp():
    return int(input())


def solution():
    (n, x) = mulinp()
    a = arrinp()
    if len(set(a)) == 1:
        if a[0] == x:
            print(0)
        else:
            print(2)
        return
    count = 0
    s = 0
    for i in range(n):
        s += a[i]
        if a[i] == x:
            count += 1
    if count != 0:
        print(1)
    elif s / n == x:
        print(1)
    else:
        print(2)
    return


testcases = 1
testcases = int(input())
for _ in range(testcases):
    solution()
