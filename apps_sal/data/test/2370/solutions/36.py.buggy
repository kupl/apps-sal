import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N = ir()
A = np.array([lr() for i in range(N)])
INF = 10 ** 9
np.fill_diagonal(A, INF)
answer = 0
for i in range(N):
    for j in range(i + 1, N):
        detour = np.min(A[i] + A[j])
        if A[i, j] < detour:
            # 最短距離としてこの道路は必要
            answer += A[i, j]
        elif A[i, j] > detour:
            print((-1))
            return

print(answer)
# 05 hint
