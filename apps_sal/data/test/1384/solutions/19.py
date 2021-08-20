n = int(input())
a = list(map(int, input().split()))
p = [0] * n
p[0] = a[0]
for i in range(1, n):
    p[i] = p[i - 1] + a[i]
ans = min(n, n - p[n - 1])
for i in range(n):
    l = p[i]
    r = n - i - 1 - (p[n - 1] - p[i])
    ans = min(ans, l + r)
print(n - ans)
