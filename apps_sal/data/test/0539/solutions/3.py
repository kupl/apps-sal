n = int(input().strip())
a = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        k = i ^ j
        if i + j > k and i + k > j and j + k > i and k <= n and k > i and k > j:
            # print(i,j,k)
            a += 1
print(a)
