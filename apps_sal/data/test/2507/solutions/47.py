import numpy as np
import sys
readline = sys.stdin.readline


N, K = map(int, readline().split())
A = np.array(sorted(list(map(int, readline().split()))))
F = np.array(sorted(list(map(int, readline().split())), reverse=True))

ok = A[-1] * F[0]
ng = -1


def isOk(x):
    # 時間がxになるためには、A_iをx/F_i以下まで減らす必要がある
    return A.sum() - np.minimum(A, x // F).sum() <= K


while (ok - ng) > 1:
    mid = (ok + ng) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid
print(ok)
