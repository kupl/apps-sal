import numpy as np

N = int(input())
A = list(map(int, input().split()))

B = np.sort(np.array([x - (i + 1) for i, x in enumerate(A)]))
if N % 2 == 1:
    b = np.median(B)
    ans = int(abs(B - b).sum())
else:
    b1 = B[N // 2 - 1]
    b2 = B[N // 2]
    ans = int(min(abs(B - b1).sum(), abs(B - b2).sum()))
    
print(ans)
