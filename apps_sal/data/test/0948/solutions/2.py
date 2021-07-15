n, m = list(map(int, input().split()))
ans = 0
A = [input() for i in range(n)]
for i in range(n - 1):
    for j in range(m - 1):
        if sorted(A[i][j] + A[i][j + 1] + A[i + 1][j] + A[i + 1][j + 1]) == sorted("face"):
            ans += 1
print(ans)


