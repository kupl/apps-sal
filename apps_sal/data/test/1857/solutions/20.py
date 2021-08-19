n = int(input())
ans = 1
for i in range(n, n - 5, -1):
    ans *= i * i
for i in range(1, 6):
    ans //= i
print(ans)
