def M(x, y):
    return [[1, 2, 1], [2, 0, 0], [1, 0, 0]][x][y]


n = int(input())
a = [list(map(int, input().split()))]
for i in range(n - 1):
    a.append([int(input())])
    if i < 3:
        for j in range(n - 1):
            a[i + 1].append(M(a[i][j + 1], a[i + 1][j]))
    else:
        for j in range(min(4, n) - 1):
            a[i + 1].append(M(a[i][j + 1], a[i + 1][j]))
A = [0, 0, 0]
for i in range(n):
    for j in range(len(a[i])):
        if i >= 3 and j >= 3:
            A[a[i][j]] += n - max(i, j)
        else:
            A[a[i][j]] += 1
print(*A)
