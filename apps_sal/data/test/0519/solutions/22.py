import sys
from collections import deque


def read():
    return list(map(int, sys.stdin.readline().split()))


(l,) = read()
(p,) = read()
(q,) = read()
print(l * p / (p + q))
