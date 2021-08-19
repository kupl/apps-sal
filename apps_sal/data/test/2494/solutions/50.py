import io
import math
import scipy.sparse
import numpy
from collections import deque
q = deque()
K = int(input())
q += [(1, 1)]
m = {}
while len(q):
    (n, s) = q.pop()
    if not n in m:
        m[n] = s
        q += [(n * 10 % K, s)]
        q.appendleft(((n + 1) % K, s + 1))
print(m[0])
