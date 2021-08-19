(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
p = [0] * m
for i in range(n):
    p[a[i] - 1] += 1
ans = 0
for i in range(m):
    ans += p[i] * (n - p[i])
print(ans // 2)
