n = int(input())
print(n + n // 2)

k = 1 - (n % 2)
rs = []
for i in range(1, n + 1):
    if i % 2 == k:
        rs.append(i)
for i in range(1, n + 1):
    if i % 2 != k:
        rs.append(i)
for i in range(1, n + 1):
    if i % 2 == k:
        rs.append(i)
print(' '.join(list(map(str, rs))))

