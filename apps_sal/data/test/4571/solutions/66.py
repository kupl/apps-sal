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


(n, m) = readInts()
ans = (1900 * m + (n - m) * 100) * 2 ** m
print(ans)
