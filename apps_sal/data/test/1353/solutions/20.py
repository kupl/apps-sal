(n, m, a, b) = map(int, input().split())
ans = 0
if m * a >= b:
    ans += n // m * b
    n = n % m
if a * n > b and m >= n:
    ans += b
    n = 0
ans += n * a
print(ans)
