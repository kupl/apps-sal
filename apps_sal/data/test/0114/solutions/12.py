import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(n)]
B = [[0] * m for i in range(n)]
ANS = []
for i in range(n - 1):
    for j in range(m - 1):
        if A[i][j] == A[i + 1][j] == A[i][j + 1] == A[i + 1][j + 1] == 1:
            ANS.append((i + 1, j + 1))
            B[i][j] = B[i + 1][j] = B[i][j + 1] = B[i + 1][j + 1] = 1
if A != B:
    print(-1)
else:
    print(len(ANS))
    for ans in ANS:
        print(*ans)
