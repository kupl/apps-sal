(n, m) = map(int, input().split())
z = [0] * m
if n >= m:
    for i in range(1, 1 + m):
        z[i * i % m] += n // m
for i in range(1, 1 + n % m):
    z[i * i % m] += 1
ans = 0
for i in range(m):
    q = (m - i) % m
    ans += max(z[i] * z[q], 0)
print(ans)
