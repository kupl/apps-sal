n = int(input())
print(sum(i - j < i ^ j < j for i in range(1, n + 1)for j in range(i)))
