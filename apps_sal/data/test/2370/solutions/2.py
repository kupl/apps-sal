import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N = ir()
INF = 10 ** 9
A = np.array([lr() for _ in range(N)])
np.fill_diagonal(A, INF)
answer = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        detour = np.min(A[i] + A[j])
        if detour > A[i, j]:
            answer += A[i, j]
        elif detour < A[i, j]:
            print((-1))
            return

print(answer)
# 38
