import sys
f = sys.stdin
n = int(f.readline().strip())
d = [[1] * n for it in range(n)]
for i in range(1, n):
    for j in range(1, n):
        d[i][j] = d[i - 1][j] + d[i][j - 1]
print(d[n - 1][n - 1])
