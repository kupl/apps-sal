import numpy as np
(n, k) = map(int, input().split())
a = [0] + list(map(int, input().split()))
a = list(np.cumsum(a))
cnt = 0
x = 1
for i in range(n):
    for j in range(x, n + 1):
        if a[j] - a[i] >= k:
            cnt += n + 1 - j
            x = j
            break
print(cnt)
