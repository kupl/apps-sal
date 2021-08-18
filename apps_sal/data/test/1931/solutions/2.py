import sys
import heapq
import math
import bisect


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def rinput():
    return map(int, input().split())


def rlinput():
    return list(map(int, input().split()))


def srlinput():
    return sorted(list(map(int, input().split())))


q = [2]
i = 2
while q[-1] < 1e9:
    q.append(q[-1] + 2 * i + i - 1)
    i += 1


def main():
    n = iinput()
    res = 0
    while n >= q[0]:
        n -= q[bisect.bisect_right(q, n) - 1]
        res += 1
    print(res)


for sdfghjkl in range(iinput()):
    main()
