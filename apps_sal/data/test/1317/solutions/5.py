(n, m) = list(map(int, input().split()))
cnt = [0] * m
for i in range(m):
    cnt[i] = n // m
    if i == 0:
        cnt[i] -= 1
    if i <= n % m:
        cnt[i] += 1
r = 0
for i in range(m):
    for j in range(m):
        if (i ** 2 + j ** 2) % m == 0:
            r += cnt[i] * cnt[j]
print(r)
