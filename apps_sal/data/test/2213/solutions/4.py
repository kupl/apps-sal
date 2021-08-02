n, m, k = map(int, input().split())
print(str(m * (m - 1) // 2))
for i in range(m):
    for j in range(m - i - 1):
        if k == 0:
            print(str(i + 1) + ' ' + str(i + j + 2))
        else:
            print(str(i + j + 2) + ' ' + str(i + 1))
