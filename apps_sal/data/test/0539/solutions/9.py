n = int(input())
sum = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        tmp = i ^ j
        if tmp >= 1 and tmp <= n and (tmp > i) and (tmp > j) and (i + j > tmp):
            sum += 1
print(sum)
