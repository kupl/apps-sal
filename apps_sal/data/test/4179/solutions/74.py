import numpy as np
(n, m, c) = map(int, input().split())
b = np.array(list(map(int, input().split())))
cnt = 0
for i in range(n):
    a = np.array(list(map(int, input().split())))
    if np.dot(a, b) + c > 0:
        cnt += 1
print(cnt)
