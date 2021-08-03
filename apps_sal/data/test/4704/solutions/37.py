import numpy as np
n = int(input())
al = list(map(int, input().split()))
bl = list(np.cumsum(al))

ans = 1001001001001
for i in range(n - 1):
    ans = min(ans, abs(bl[i] - (bl[-1] - bl[i])))
print(ans)
