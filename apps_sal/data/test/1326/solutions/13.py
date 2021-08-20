n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += (i + i * (n // i)) * (n // i) // 2
print(ans)
