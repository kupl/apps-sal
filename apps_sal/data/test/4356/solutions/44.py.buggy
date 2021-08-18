import sys


N, M = [int(x) for x in input().split()]
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

for i in range(N - M + 1):
    for j in range(N - M + 1):
        found = True
        for _i in range(M):
            for _j in range(M):
                if A[i + _i][j + _j] != B[_i][_j]:
                    found = False
                    break
            if not found:
                break
        if found:
            print('Yes')
            return
print('No')
