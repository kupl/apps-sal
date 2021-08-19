import numpy as np
(n, m) = map(int, input().split())
ans = [0] * n
for _ in range(m):
    (l, r) = map(int, input().split())
    ans[l - 1] += 1
    if r < n:
        ans[r] -= 1
c = list(np.cumsum(ans))
print(c.count(m))
