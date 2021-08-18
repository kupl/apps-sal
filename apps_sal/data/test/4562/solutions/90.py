
n = int(input())

ans = 1
for i in range(1, n + 1):
    if (i * i > n):
        ans = (i - 1)**2
        break
print(ans)
