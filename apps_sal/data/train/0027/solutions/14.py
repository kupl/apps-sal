import sys
import math
import heapq


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def tinput():
    return input().split()


def rinput():
    return list(map(int, tinput()))


def rlinput():
    return list(rinput())


def main():
    n, w, q, res = iinput(), set(), [], 0
    for i in rinput():
        if i % 2 == 0:
            if i not in w:
                w.add(i)
                heapq.heappush(q, -i)
    while q:
        i = -heapq.heappop(q) // 2
        res += 1
        if i % 2 == 0:
            if i not in w:
                w.add(i)
                heapq.heappush(q, -i)

    print(res)


for i in range(iinput()):
    main()
