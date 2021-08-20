import numpy as np
from collections import Counter
n = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
b = np.array([0] * (max(A) + 1))
A.sort()
ans = 0
for a in A:
    if cnt[a] == 1 and (not b[a]):
        ans += 1
    b[a::a] = 1
print(ans)
