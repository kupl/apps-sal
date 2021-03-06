import sys
import numpy as np
from collections import defaultdict


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


(N, K) = lr()
A = np.array([1] + lr())
A = (A - 1) % K
N += 1
Acum = (A.cumsum() % K).tolist()
d = defaultdict(int)
answer = 0
for (i, x) in enumerate(Acum):
    answer += d[x]
    d[x] += 1
    if i >= K - 1:
        d[Acum[i - (K - 1)]] -= 1
print(answer)
