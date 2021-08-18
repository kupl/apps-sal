import sys
import numpy as np
from collections import defaultdict


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N, K = lr()
A = np.array([1] + lr())
A = (A - 1) % K
Acum = A.cumsum() % K
counter = defaultdict(int)
answer = 0
for i in range(len(Acum)):
    x = Acum[i]
    answer += counter[x]
    counter[x] += 1
    if i >= K - 1:
        counter[Acum[i - (K - 1)]] -= 1

print(answer)
