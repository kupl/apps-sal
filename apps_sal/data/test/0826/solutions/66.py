n = int(input()) + 1
a = int(((8 * n + 1) ** 0.5 - 1) // 2)
ans = 0
for i in range(max(0, a - 100), a + 100):
    if i * (i + 1) <= 2 * n and 2 * n < (i + 1) * (i + 2):
        ans = n - i
        break
print(ans)
