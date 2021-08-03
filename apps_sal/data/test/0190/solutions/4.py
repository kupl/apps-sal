n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(input()))
minj, maxi, maxj, mini = 10000000000000, 0, -1, 1000000000000
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            minj = min(j, minj)
            maxi = i
            maxj = max(maxj, j)
            mini = min(mini, i)
print(max(maxi - mini + 1, maxj - minj + 1))
