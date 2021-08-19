(n, m) = list(map(int, input().split()))
a = [input().strip() for x in range(n)]
print(sum((set([a[i][j], a[i + 1][j], a[i][j + 1], a[i + 1][j + 1]]) == set('face') for i in range(n - 1) for j in range(m - 1))))
