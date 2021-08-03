import sys

n = int(sys.stdin.readline().strip())
A = []
for i in range(0, n):
    A.append(sys.stdin.readline().strip())
D = [[-200 for i in range(0, n)] for j in range(0, n)]
L = []
L2 = []
for i in range(0, n):
    D[i][i] = 0
    L.append([i, i])
for i in range(0, n):
    while len(L) > 0:
        x, y = L.pop()
        for j in range(0, n):
            if A[y][j] == "1" and D[x][j] == -200:
                D[x][j] = i + 1
                L2.append([x, j])
    L = L2[:]
    L2 = []

m = int(sys.stdin.readline().strip())
p = list(map(int, sys.stdin.readline().strip().split()))
k = 1
ans = []
i = 0
j = 1
while j < m - 1:
    if D[p[i] - 1][p[j + 1] - 1] == j + 1 - i:
        j = j + 1
    else:
        ans.append(p[i])
        i = j
        j = j + 1
ans.append(p[i])
if i != m - 1:
    ans.append(p[m - 1])
print(len(ans))
print(" ".join(list(map(str, ans))))
