n, a, b, c, d = list(map(int, input().split()))
lo = min(a+b, a+c, c+d, b+d)
hi = max(a+b, a+c, c+d, b+d)
ans = 0
for x in range(1, n+1):
    ans += max(0, n-(hi-lo))
print(ans)

