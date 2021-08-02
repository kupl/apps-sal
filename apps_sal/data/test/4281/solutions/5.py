import sys
from operator import itemgetter
from collections import deque


def input():
    return sys.stdin.readline().strip()


def getmin(houses):
    i = 0
    ans = 0
    while len(houses) > 0:
        x = houses.popleft()
        while len(houses) > 0 and houses[0] <= x + 2:
            houses.popleft()
        ans += 1
    return ans


def getmax(houses):
    vis = set()
    for x in houses:
        if x - 1 not in vis:
            vis.add(x - 1)
        elif x not in vis:
            vis.add(x)
        else:
            vis.add(x + 1)
    return len(vis)


n = int(input())

houses = list(map(int, input().split()))
houses.sort()
print(getmin(deque(houses)), getmax(houses))
