import sys
from collections import deque
import heapq


def input(): return sys.stdin.readline().strip()


ipnut = input
def pprint(x): return print(' '.join(map(lambda t: str(t + 1), x)))


def mex():
    used = set(a)
    for i in range(n + 1):
        if i not in used:
            return i


for _ in range(int(input())):
    n = int(input())
    f = False
    for i in range(int(n ** 0.5)):
        i += 2
        if n % i == 0:
            print(n // i, n - n // i)
            f = True
            break
    if f:
        pass
    else:
        print(1, n - 1)
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
