n, k = list(map(int, input().split()))
matrix = []
for i in range(n):
    matrix.append(list(input()))
spree = 0
counts = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '#':
            spree = 0
        else:
            spree += 1
            if spree == k:
                for z in range(j - k + 1, j + 1):
                    counts[i][z] += 1
                spree = k - 1
    spree = 0
for i in range(n):
    for j in range(n):
        if matrix[j][i] == '#':
            spree = 0
        else:
            spree += 1
            if spree == k:
                for z in range(j - k + 1, j + 1):
                    counts[z][i] += 1
                spree = k - 1
    spree = 0
ans1, ans2 = 0, 0
for i in range(n):
    for j in range(n):
        if counts[i][j] > counts[ans1][ans2]:
            ans1 = i
            ans2 = j
print("{} {}".format(ans1 + 1, ans2 + 1))
