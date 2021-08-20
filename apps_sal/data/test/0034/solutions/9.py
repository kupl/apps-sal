(n, a, b) = list(map(int, input().split()))
ans = 0
for x in range(1, n):
    ans = max(ans, min(a // x, b // (n - x)))
print(ans)
