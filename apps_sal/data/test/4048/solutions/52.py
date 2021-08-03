n = int(input())
ans = int(1e18)
for i in range(1, n):
    if i * i <= n:
        if n % i == 0:
            j = int(n / i)
            ans = min(ans, i + j - 2)
    else:
        break
print(ans)
