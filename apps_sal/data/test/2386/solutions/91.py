import numpy as np
import statistics
n = int(input())
a = list(map(int, input().split()))
a = np.array(a, dtype=int)
one = np.ones(n, dtype=int)
stairs = np.add.accumulate(one)
a = a - stairs
b = int(statistics.median(a))


def pos(b):
    return sum(abs(a - b))


print(pos(b))
