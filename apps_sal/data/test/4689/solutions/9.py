import numpy as np
(k, n) = map(int, input().split())
a = list(map(int, input().split()))
dist = [a[i + 1] - a[i] if i < n - 1 else k - a[i] + a[0] for i in range(n)]
max_index = np.argmax(dist)
cost = 0
curr_index = max_index
for _ in range(n - 1):
    if curr_index == 0:
        cost += a[curr_index] + k - a[curr_index - 1]
    else:
        cost += a[curr_index] - a[curr_index - 1]
    curr_index -= 1
print(cost)
