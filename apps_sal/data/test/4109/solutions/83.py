import itertools
import numpy as np
import copy

N, M, X = list(map(int, input().split()))
CA = [list(map(int, input().split())) for _ in range(N)]
CA = np.array(CA)

ans = 10 ** 7
for i in itertools.product([0, 1], repeat=N):
    tCA = copy.copy(CA)
    for j in range(N):
        if i[j] == 0:
            tCA[j] = np.zeros(CA.shape[1])
    s = np.sum(tCA, axis=0)
    l = sum(k >= X for k in s[1:])
    if s[0] < ans and l == M:
        ans = s[0]

if ans == 10 ** 7:
    print((-1))
else:
    print(ans)

