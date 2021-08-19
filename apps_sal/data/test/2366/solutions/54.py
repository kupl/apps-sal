import numpy as np
n = int(input())
A = list(map(int, input().split()))
c = np.zeros(n + 1, dtype=np.int32)
for a in A:
    c[a] += 1
aa = list(set(A))
allsum = 0
for a in aa:
    allsum += c[a] * (c[a] - 1) // 2
for a in A:
    print(allsum - c[a] + 1)
