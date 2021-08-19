import sys
import numpy as np
sys.setrecursionlimit(10000)
INF = float('inf')
N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
A = np.array(A, dtype=float) + np.diag([np.inf] * N)
useless = np.zeros((N, N), dtype=bool)
impossible = np.zeros((N, N), dtype=bool)
for via in range(N):
    R = sum(np.meshgrid(A[via], A[via]))
    useless |= R == A
    impossible |= R < A
if (impossible ^ np.eye(N, dtype=bool)).sum():
    print(-1)
else:
    print(int(A[~useless].sum() // 2))
