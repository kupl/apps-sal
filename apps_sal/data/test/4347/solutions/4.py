n = int(input())
ans = 1
for i in range(1, n):
    ans *= i
ans //= n // 2
print(ans)
