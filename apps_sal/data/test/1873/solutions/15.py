(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
count = 0
for i in range(m):
    for j in range(i + 1, m):
        count += a.count(i + 1) * a.count(j + 1)
print(count)
