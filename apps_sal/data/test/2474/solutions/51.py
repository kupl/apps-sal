import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N = ir()
C = np.array(lr())
MOD = 10 ** 9 + 7
C.sort()
two_power = np.array([(1 + N - i) * pow(2, (N - 2), MOD) % MOD if i < N - 1 else pow(2, i, MOD) for i in range(N)])
answer = (C * two_power % MOD).sum() % MOD * pow(2, N, MOD)
print((answer % MOD))
