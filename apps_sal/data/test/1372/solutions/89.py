import numpy as np
(h, n) = map(int, input().split())
attack = [0] * n
magic = [0] * n
for i in range(n):
    (a, b) = map(int, input().split())
    attack[i] = a
    magic[i] = b
attack = np.array(attack)
mgic = np.array(magic)
lim = 0
dp = [lim] * (h + 1)
dp = np.array(dp)
dp[0] = 0
for i in range(1, h + 1):
    temp = dp[np.maximum(i - attack, 0)] + magic
    dp[i] = np.min(temp)
print(dp[h])
