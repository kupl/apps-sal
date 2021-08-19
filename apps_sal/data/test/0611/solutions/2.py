import time
from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque
from collections import Counter


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


(n, m) = readmap()
X = []
D = []
for _ in range(m):
    (x, d) = readmap()
    X.append(x)
    D.append(d)
summ = n * sum(X)
for i in range(m):
    d = D[i]
    if d < 0:
        if n % 2 == 1:
            summ += d * (n // 2) * (n // 2 + 1)
        else:
            summ += d * (n // 2) * (n // 2)
    else:
        summ += d * (n - 1) * n // 2
print(summ / n)
