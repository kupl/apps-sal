n = int(input())
d = list(map(int, input().split()))
sum = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        sum += d[i] * d[j]
print(sum)
