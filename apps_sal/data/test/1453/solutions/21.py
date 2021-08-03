n, m = map(int, input().split())
a = [0] + sorted(map(int, input().split()))
ma = [0] * m
total = 0
ans = [0] * n

for i in range(1, n + 1):
    ma[i % m] += a[i]
    total += ma[i % m]
    ans[i - 1] = total

print(*ans)
