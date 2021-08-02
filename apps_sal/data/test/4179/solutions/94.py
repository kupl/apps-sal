n, m, c = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for i in range(n):
    total = c
    a = list(map(int, input().split()))
    for j in range(m):
        total += a[j] * b[j]
    if total > 0:
        count += 1
print(count)
