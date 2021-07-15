import numpy as np
import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

n, m = list(map(int, input().split()))
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

weight_n = np.array([(i + 1) * (n - i - 1) % MOD for i in range(n - 1)]).astype(np.int64)
weight_m = np.array([(i + 1) * (m - i - 1) % MOD for i in range(m - 1)]).astype(np.int64)

dxs = np.array([xs[i+1] - xs[i] for i in range(n-1)]).astype(np.int64)
dys = np.array([ys[i+1] - ys[i] for i in range(m-1)]).astype(np.int64)

t_x = np.sum(weight_n * dxs % MOD) % MOD
t_y = np.sum(weight_m * dys % MOD) % MOD

print((t_x * t_y % MOD))

