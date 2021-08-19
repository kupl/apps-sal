import numpy as np
k = int(input())
ans = np.array([i for i in range(50)], dtype=np.int64)
a = k // 50
b = k % 50
ans += a
for i in range(b):
    ans[i] += 50
    ans[:i] -= 1
    ans[i + 1:] -= 1
print(50)
print(' '.join(map(str, ans)))
