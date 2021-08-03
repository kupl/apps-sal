n = int(input())
sum = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j >= i ^ j > i - j:
            sum += 1
print(sum)
