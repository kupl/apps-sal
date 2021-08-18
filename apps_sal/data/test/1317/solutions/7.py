n, m = list(map(int, input().split()))
cnt = [0 for _ in range(m)]
for x in range(min(m, n + 1)):
    z = n // m
    if n % m >= x:
        z += 1
    cnt[x * x % m] += z
cnt[0] -= 1
res = 0
for i in range(m):
    res += cnt[i] * cnt[(m - i) % m]
print(res)
