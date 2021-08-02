n, k, m = list(map(int, input().split()))
a = [int(x) for x in input().split()]
a.sort(reverse=True)

ans = 0
s = 0
for i in range(n):
    s += a[i]
    if n - i - 1 > m:
        continue
    ans = max(ans, float((s + min(m - (n - i - 1), (i + 1) * k)) / (i + 1)))
print(ans)
