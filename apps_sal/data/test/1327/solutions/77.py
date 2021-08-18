import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


N, M = LI()
A = [LI() for _ in range(N)]
m = [[0] * 3 for _ in range(8)]

A.sort(key=lambda x: x[0] + x[1] + x[2])
for i in range(M):
    for j in range(3):
        m[0][j] += A[i][j]
        m[1][j] += A[N - 1 - i][j]

A.sort(key=lambda x: x[0] + x[1] - x[2])
for i in range(M):
    for j in range(3):
        m[2][j] += A[i][j]
        m[3][j] += A[N - 1 - i][j]

A.sort(key=lambda x: x[0] - x[1] + x[2])
for i in range(M):
    for j in range(3):
        m[4][j] += A[i][j]
        m[5][j] += A[N - 1 - i][j]

A.sort(key=lambda x: x[0] - x[1] - x[2])
for i in range(M):
    for j in range(3):
        m[6][j] += A[i][j]
        m[7][j] += A[N - 1 - i][j]

print((max([abs(x[0]) + abs(x[1]) + abs(x[2]) for x in m])))
