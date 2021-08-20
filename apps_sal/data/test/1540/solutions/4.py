(n, m, k) = map(int, input().split())
matrix = []
for i in range(n):
    mat = list(map(int, input().split()))
    matrix.append(mat)
mat = [0 for i in range(m + 1)]
ans = [0 for i in range(n + 1)]
for i in range(k):
    (a, b) = map(int, input().split())
    mat[b - 1] += 1
    ans[a - 1] -= 1
for i in range(n):
    s = sum([mat[j] for j in range(m) if matrix[i][j] == 1])
    print(ans[i] + s, end=' ')
