n = int(input())

ans = n * (n + 1) - 1
i = 2
while i * i <= n:
    m = n // i
    ans += i * (m * m - i * i + m)
    i += 1
print(ans)
