import sys
(n, m) = list(map(int, sys.stdin.readline().strip().split()))
s = []
for i in range(0, n):
    s.append(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
ans = 0
for j in range(0, m):
    (A, B, C, D, E) = (0, 0, 0, 0, 0)
    for i in range(0, n):
        if s[i][j] == 'A':
            A = A + 1
        if s[i][j] == 'B':
            B = B + 1
        if s[i][j] == 'C':
            C = C + 1
        if s[i][j] == 'D':
            D = D + 1
        if s[i][j] == 'E':
            E = E + 1
    ans = ans + max([A, B, C, D, E]) * a[j]
print(ans)
