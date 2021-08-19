from collections import defaultdict
from collections import deque
from collections import Counter
import math


def readInt():
    return int(input())


def readInts():
    return list(map(int, input().split()))


def readChar():
    return input()


def readChars():
    return input().split()


(n, x, y) = readInts()
d = defaultdict(int)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        d[min(abs(i - j), abs(i - x) + 1 + abs(y - j), abs(i - y) + 1 + abs(j - x))] += 1
for i in range(1, n):
    print(d[i])
