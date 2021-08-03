n = int(input())
ans = sum((n - l + 1) * (n - l + 2) // 2 for l in range(1, n + 1))
for i in range(n - 1):
    a, s = map(int, input().split())
    if a > s:
        a, s = s, a
    ans -= a * (n + 1 - s)
print(ans)
