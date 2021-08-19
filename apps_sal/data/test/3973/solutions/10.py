n, m = map(int, input().split())
a = list(map(int, input().split()))

imos = [0] * (2 * m + 2)
ans = 0
for i in range(n - 1):
    a0 = a[i] - 1
    a1 = a[i + 1] - 1
    dif = (a1 - a0) % m
    ans += dif
    if(dif >= 2):
        imos[a0 + 2] += 1
        imos[a0 + dif + 1] -= dif
        imos[a0 + dif + 2] += dif - 1

# print(imos)

for i in range(1, 2 * m + 2):
    imos[i] += imos[i - 1]
# print(imos)

for i in range(1, 2 * m + 2):
    imos[i] += imos[i - 1]
# print(imos)

for i in range(m):
    imos[i] += imos[i + m]

ans -= max(imos[:m])
print(ans)
