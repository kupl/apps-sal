from scipy.sparse.csgraph import floyd_warshall
n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for i in range(m)]
q = int(input())
S = [list(map(int, input().split())) for i in range(q)]


for i in range(m):
    for j in range(2):
        A[i][j] -= 1

for i in range(q):
    for j in range(2):
        S[i][j] -= 1

M = [[float("inf")] * n for i in range(n)]

for i in range(n):
    M[i][i] = 0

for i in range(m):
    M[A[i][0]][A[i][1]] = A[i][2]
    M[A[i][1]][A[i][0]] = A[i][2]


M = floyd_warshall(M)

for i in range(n):
    for j in range(n):
        M[i][j] = 1 if M[i][j] <= l else float("inf")

for i in range(n):
    M[i][i] = 0


M = floyd_warshall(M)

for i in range(q):
    ans = M[S[i][0]][S[i][1]] - 1
    if ans == float("inf"):
        ans = -1
    print(int(ans))
