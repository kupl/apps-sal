import numpy as np
s = input()

A = []
for i in range(6):
    m = [-(j*10**i%13)%13 for j in range(10)]
    tmp = []
    for j in m:
        tmp.append([[1 if (k-l)%13==j else 0 for k in range(13)] for l in range(13)])
    tmp.append([[1 if (k-l)%13 in m else 0 for k in range(13)] for l in range(13)])
    A.append(tmp)
A = np.array(A)

dp = np.zeros(13, dtype=int)
dp[0] = 1
m = 1
for ind, i in enumerate(reversed(s)):
    i = int(i) if i!='?' else 10
    tmp = np.dot(A[ind%6, i, :, :], dp)
    dp = tmp%(10**9+7)
print((dp[5]))

