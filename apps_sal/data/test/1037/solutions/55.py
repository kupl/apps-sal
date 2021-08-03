import numpy as np

n = int(input())
A = list(map(int, input().split()))

babies = sorted([(activity, index) for index, activity in enumerate(A, 1)], reverse=True)

DP = np.zeros(n + 1, dtype=np.int64)
position = np.arange(1, n + 1, dtype=np.int64)

for filled, (activity, index) in enumerate(babies, 1):
    to_left = DP[:filled] + abs((position[:filled] - index) * activity)
    to_right = DP[:filled] + abs((position[-filled:] - index) * activity)
    DP[1:filled + 1] = np.maximum(DP[1:filled + 1], to_left)
    DP[:filled] = np.maximum(DP[:filled], to_right)

print((DP.max()))
