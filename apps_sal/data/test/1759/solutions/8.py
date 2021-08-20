import sys
(m, n) = list(map(int, sys.stdin.readline().split()))
T = []
for i in range(m):
    T.append(list(map(int, sys.stdin.readline().split())))
C = [0] * n
Ans = ''
for i in range(m):
    t = C[0]
    for j in range(n):
        if t < C[j]:
            t = C[j] + T[i][j]
        else:
            t += T[i][j]
        C[j] = t
    Ans += str(t) + ' '
sys.stdout.write(Ans)
