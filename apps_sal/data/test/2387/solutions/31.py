from heapq import heappop, heappush
import sys
from operator import itemgetter
sysread = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10 ** 7)


def run():
    N = int(input())
    current = 0
    ways = []
    dic = {'(': 1, ')': -1}
    SS = read().split()
    for S in SS:
        path = [0]
        for s in S:
            path.append(path[-1] + dic[s])
        ways.append((path[-1], min(path)))
    ways_pos = sorted([(a, b) for (a, b) in ways if a >= 0], key=lambda x: (x[1], x[0]), reverse=True)
    ways_neg = sorted([(a, b) for (a, b) in ways if a < 0], key=lambda x: (x[1] - x[0], -x[0]), reverse=True)[::-1]
    for (go, max_depth) in ways_pos:
        if current + max_depth >= 0:
            current += go
        else:
            print('No')
            return None
    for (go, max_depth) in ways_neg:
        if current + max_depth >= 0:
            current += go
        else:
            print('No')
            return None
    if current == 0:
        print('Yes')
    else:
        print('No')


def __starting_point():
    run()


__starting_point()
