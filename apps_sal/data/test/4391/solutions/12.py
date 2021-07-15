n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [0]
for i in range(n):
    b.append(a[i] + b[i])
max1 = 0
for i in range(k, n + 1):
    for j in range(1, n - i + 2):
        max1 = max(max1, (b[j + i - 1] - b[j - 1]) / i)
print(max1)

