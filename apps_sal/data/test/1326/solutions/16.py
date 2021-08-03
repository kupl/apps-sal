n = int(input())
cnt = 0
for i in range(1, n + 1):
    cnt += i * (n // i) * (n // i + 1) // 2
print(cnt)
