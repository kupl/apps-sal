from collections import defaultdict
from collections import deque
from collections import Counter
import itertools
import math


def readInt():
    return int(input())


def readInts():
    return list(map(int, input().split()))


def readChar():
    return input()


def readChars():
    return input().split()


n = readInt()
sn = [list(input()) for i in range(n)]
ans = ''
for i in range(97, 123):
    m = float('inf')
    for j in sn:
        m = min(m, j.count(chr(i)))
    ans += chr(i) * m
print(ans)
