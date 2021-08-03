from collections import defaultdict
from queue import deque


def arrinp():
    return [*list(map(int, input().split(' ')))]


def mulinp():
    return list(map(int, input().split(' ')))


def intinp():
    return int(input())


def solution():
    x, y, k = mulinp()
    num = y * k + k
    ans = (num - 1) // (x - 1)
    if (num - 1) % (x - 1) != 0:
        ans += 1
    ans += k
    print(ans)


testcases = 1
testcases = int(input())
for _ in range(testcases):
    solution()
