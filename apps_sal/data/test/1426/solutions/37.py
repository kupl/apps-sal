import sys
from collections import deque
N, M = map(int, input().split())
A = [[]for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    A[a - 1].append(b - 1)
S, T = map(int, input().split())
sys.setrecursionlimit(10**7)  # 再帰制限のとっぱらい
D = [[-1] * 3 for i in range(N)]


def bfs(x, n):
    q = deque()
    q.append((x, n))
    while len(q):
        x, n = q.popleft()
        for i in A[x]:
            d = (n + 1) % 3
            if D[i][d] == -1:
                D[i][d] = D[x][n] + 1
                q.append((i, d))


D[S - 1][0] = 0
bfs(S - 1, 0)
if D[T - 1][0] == -1:
    print(-1)
else:
    print(D[T - 1][0] // 3)
