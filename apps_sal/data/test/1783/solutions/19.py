import sys
import os
import math
(n, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
if n == k:
    print(sum(A))
elif n - k >= k:
    v = 0
    for i in range(n):
        if i < k:
            v += (i + 1) * A[i]
        elif n - k < i:
            v += (n - i) * A[i]
        else:
            v += k * A[i]
    ans = v / (n - k + 1)
    print(ans)
else:
    v = 0
    for i in range(n):
        if i < n - k:
            v += (i + 1) * A[i]
        elif k <= i:
            v += (n - i) * A[i]
        else:
            v += (n - k + 1) * A[i]
    ans = v / (n - k + 1)
    print(ans)
