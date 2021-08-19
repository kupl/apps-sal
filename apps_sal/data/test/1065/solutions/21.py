(n, k, m, d) = map(int, input().split())
ans = 0
for x in range(1, d + 1):
    y = min(n // ((x - 1) * k + 1), m)
    ans = max(ans, x * y)
print(ans)
