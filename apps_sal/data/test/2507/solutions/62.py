import numpy as np
(N, K) = map(int, input().split())
A = np.array(input().split(), np.int64)
F = np.array(input().split(), np.int64)
A.sort()
F.sort()
F = F[::-1]
dig = A.sum()


def judge(x):
    return dig - np.minimum(A, x // F).sum() <= K


l = -1
r = 10 ** 18 + 1
while l + 1 < r:
    test = (l + r) // 2
    if judge(test):
        r = test
    else:
        l = test
print(r)
