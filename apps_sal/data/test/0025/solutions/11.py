n, k = map(int, input().split())

mat = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j and k > 0:
            mat[i][j] = 1
            k -= 1
        elif i < j and k > 1:
            mat[i][j] = mat[j][i] = 1
            k -= 2
if k > 0:
    print(-1)
    return

print("\n".join(" ".join(map(str, e)) for e in mat))
