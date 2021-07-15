n, m, k = map(int, input().split())
a = [[0] * (m + 2) for i in range(n + 2)]
for c in range(k):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    a[i][j] = 1
    for i1 in range(i - 1, i + 1):
        for j1 in range(j - 1, j + 1):
            if a[i1][j1] == a[i1 + 1][j1 + 1] == a[i1 + 1][j1] == a[i1][j1 + 1] == 1:
                print(c + 1)
                return
print(0)
