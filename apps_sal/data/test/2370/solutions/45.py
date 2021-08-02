import numpy as np
n = int(input())
a = np.array([list(map(int, input().split())) for _ in range(n)])
ans = 0
for i in range(n):
    a[i][i] = 10**9 + 1
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        dp = np.min(a[i] + a[j])
        if a[i][j] < dp:
            ans += a[i][j]
        elif a[i][j] > dp:
            print(-1)
            return
print(ans)
