n = int(input())
maxn = int(n ** (1 / 3))
count = 0
for i in range(1, n + 1, 2):
    tmp = 0
    for j in range(1, i + 1):
        if i % j == 0:
            tmp += 1
    if tmp == 8:
        count += 1
print(count)
