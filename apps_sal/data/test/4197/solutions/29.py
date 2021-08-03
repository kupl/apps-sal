import numpy as np

n = int(input())
a = list(map(int, input().split()))

ans = np.empty(n, dtype=int)
for i in range(n):
    ans[a[i] - 1] = i + 1
print(*ans)
