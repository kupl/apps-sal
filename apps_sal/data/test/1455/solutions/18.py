n = int(input())
if n % 2 == 0:
    print(n // 2 + 1)
else:
    print((n + 1) // 2)
i = j = 1
for _ in range(1, n + 1):
    print(i, j)
    if i == j:
        j += 1
    else:
        i += 1
