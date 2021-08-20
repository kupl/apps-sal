(n, m) = map(int, input().split())
T = [[] for i in range(n)]
for i in range(n):
    a = list(input())
    T[i] = a
S = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if T[i][j] == '*':
            S[i][j] = 1
rec = []
for i in range(n):
    for j in range(m):
        if 1 <= i < n - 1 and 1 <= j < m - 1 and (T[i][j] == '*') and (T[i - 1][j] == '*') and (T[i][j - 1] == '*') and (T[i + 1][j] == '*') and (T[i][j + 1] == '*'):
            S[i][j] = 0
            S[i - 1][j] = 0
            S[i][j - 1] = 0
            S[i + 1][j] = 0
            S[i][j + 1] = 0
            k = 2
            while True:
                if not (0 <= i - k and i + k < n and (0 <= j - k) and (j + k < m)):
                    break
                if T[i - k][j] == '*' and T[i][j - k] == '*' and (T[i + k][j] == '*') and (T[i][j + k] == '*'):
                    S[i - k][j] = 0
                    S[i][j - k] = 0
                    S[i + k][j] = 0
                    S[i][j + k] = 0
                    k += 1
                else:
                    break
            rec.append((i + 1, j + 1, k - 1))
q = 0
for i in range(n):
    for j in range(m):
        q += S[i][j]
if q == 0:
    print(len(rec))
    for i in range(len(rec)):
        print('{} {} {}'.format(rec[i][0], rec[i][1], rec[i][2]))
else:
    print(-1)
