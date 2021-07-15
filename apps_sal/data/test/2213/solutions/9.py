n, m, k = map(int, input().split())
print(m * (m - 1) // 2)
for i in range(1, m):
    for j in range(i + 1, m + 1):
        if k == 0:
            print (i,j)
        else:
            print(j,i)
