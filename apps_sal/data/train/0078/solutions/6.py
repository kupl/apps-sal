import sys
input = sys.stdin.readline
Q = int(input())
for testcases in range(Q):
    (n, m) = list(map(int, input().split()))
    MAP = [list(input().strip()) for i in range(n)]
    R = [MAP[i].count('*') for i in range(n)]
    C = []
    for j in range(m):
        M = [MAP[i][j] for i in range(n)]
        C.append(M.count('*'))
    ANS = float('inf')
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == '*':
                ANS = min(ANS, n + m - R[i] - C[j])
            else:
                ANS = min(ANS, n + m - R[i] - C[j] - 1)
    print(ANS)
