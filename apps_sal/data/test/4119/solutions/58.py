(n, m) = map(int, input().split())
x = sorted(map(int, input().split()))
a = sorted([x[i] - x[i - 1] for i in range(1, m)])
ans = 0
for i in range(m - n):
    ans += a[i]
print(ans)
