import numpy as np
(n, k) = list(map(int, input().split()))
fruits = np.array(input().split(), dtype=np.int64)
fruits.sort()
ans = 0
cnt = 0
for i in fruits:
    if cnt < k:
        ans += i
        cnt += 1
print(ans)
