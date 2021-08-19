import sys
q = int(sys.stdin.readline().strip())
for t in range(0, q):
    (n, m) = list(map(int, sys.stdin.readline().strip().split()))
    L = []
    R = [0] * n
    C = [0] * m
    for i in range(0, n):
        L.append(sys.stdin.readline().strip())
        for j in range(0, m):
            if L[i][j] != '*':
                R[i] = R[i] + 1
                C[j] = C[j] + 1
    ans = n + m - 1
    for i in range(0, n):
        for j in range(0, m):
            x = 0
            if L[i][j] != '*':
                x = -1
            ans = min([ans, R[i] + C[j] + x])
    print(ans)
