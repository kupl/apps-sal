(n, m) = list(map(int, input().split(' ')))
c = list(map(int, input().split(' ')))
ans = 0
for i in range(n - 1):
    ans += c[i] * c[i + 1]
ans += c[0] * c[n - 1]
s = sum(c)
k = list(map(int, input().split(' ')))
v = [0] * n
for i in k:
    if v[i - 1]:
        continue
    v[i - 1] = 1
    s -= c[i - 1]
    ans += s * c[(i - 1 + n) % n]
    if not v[(i - 2 + n) % n]:
        ans -= c[i - 1] * c[(i - 2 + n) % n]
    if not v[i % n]:
        ans -= c[i - 1] * c[i % n]
print(ans)
