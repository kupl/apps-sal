n, m, k = list(map(int, input().split()))
print((m * (m - 1)) // 2)
for i in range(1, m):
    for j in range(i + 1, m + 1):
        if k:
            print(j, i)
        else:
            print(i, j)
