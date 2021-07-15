n, a, b, c, d = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    if c + d + 1 <= a + b + i <= c + d + n and a + c + 1 <= a + b + i <= a + c + n and b + d + 1 <= a + b + i <= b + d + n:
        ans += n
print(ans)
