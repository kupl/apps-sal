import sys
input = sys.stdin.readline

n, m, h = list(map(int, input().split()))

A = list(map(int, input().split()))

B = list(map(int, input().split()))

MAP = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        if MAP[i][j] == 0:
            continue

        MAP[i][j] = min(A[j], B[i])

for m in MAP:
    print(*m)
