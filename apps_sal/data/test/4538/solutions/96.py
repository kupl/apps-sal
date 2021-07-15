n, d = map(int, input().split())
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    if (a**2 + b**2)**0.5 <= d:
        ans += 1
print(ans)
