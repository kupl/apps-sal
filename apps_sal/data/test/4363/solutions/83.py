K, S = list(map(int, input().split()))
result = 0

for i in range(K + 1):
    for j in range(K + 1):
        if K >= S - (i + j) >= 0:
            z = S - (i + j)
            result += 1


print(result)
