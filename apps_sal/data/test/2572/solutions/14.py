import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n, m = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(n)]

    ANS = 0

    for i in range((n + 1) // 2):
        for j in range((m + 1) // 2):
            if i * 2 + 1 == n and j * 2 + 1 == m:
                continue

            elif i * 2 + 1 == n:
                X = [A[i][j], A[i][m - 1 - j]]
                ANS += abs(X[1] - X[0])

            elif j * 2 + 1 == m:
                X = [A[i][j], A[n - 1 - i][j]]
                ANS += abs(X[1] - X[0])

            else:
                X = sorted([A[i][j], A[n - 1 - i][j], A[i][m - 1 - j], A[n - 1 - i][m - 1 - j]])
                ANS += X[1] - X[0] + (X[2] - X[1]) + (X[3] - X[1])
    print(ANS)
