z, n, m = list(map(int, input().split()))
ans = 0
for i in range(1, z):
    ans = max(ans, min(n / (z - i), m / i))
print(int(ans // 1))

