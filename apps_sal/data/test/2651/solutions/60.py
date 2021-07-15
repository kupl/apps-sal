import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
n, m = lr()
X = np.array(lr())
Y = np.array(lr())
coef_x = np.arange(n)*2 - (n-1)
X *= coef_x
xsum = (X%MOD).sum() % MOD
coef_y = np.arange(m)*2 - (m-1)
Y *= coef_y
ysum = (Y%MOD).sum() % MOD
answer = xsum * ysum % MOD
print((answer % MOD))

