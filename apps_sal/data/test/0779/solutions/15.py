n = int(input())
suc = 0
for i in range(1, n // 2 + 1):
    if (n - i) // i * i == n - i:
        suc += 1
print(suc)
