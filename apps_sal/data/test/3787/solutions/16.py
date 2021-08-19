import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10 ** 7)


def input():
    return sys.stdin.readline()[:-1]


mod = 10 ** 9 + 7


def I():
    return int(input())


def LI():
    return list(map(int, input().split()))


def LIR(row, col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))


(N, A, B) = LI()
if math.ceil(N / A) <= B <= N - A + 1:
    numl = [1] * A
    numl[0] = B
    left = N - A - B + 1
    for i in range(1, A):
        val = min(left, B - 1)
        numl[i] += val
        left -= val
    ans = []
    now = 1
    for i in range(A):
        ans.extend(list(reversed(range(now, now + numl[i]))))
        now += numl[i]
    print(*ans)
else:
    print(-1)
