import numpy as np

H, N = list(map(int, input().split()))

ab = []
for i in range(N):
    a, b = list(map(int, input().split()))
    ab.append([a, b])

ab = np.array(ab)
a_list = ab[:, 0]
b_list = ab[:, 1]
max_a = ab.max()

inf = float('inf')
dp = np.array([inf for _ in range(H + max_a)])
dp[0] = 0

for i in range(1, len(dp)):
    dp[i] = np.amin(dp[np.maximum(i - a_list, 0)] + b_list)

print((int(min(dp[H:]))))
