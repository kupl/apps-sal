def comb(n, r):
    x, y = 1, 1
    for i in range(n, n - r, -1):
        x *= i
        y *= i + r - n
    return x // y


n, a, b = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
c = b - a + 1
s = [0] * c
for i in range(c):
    s[i] = sum(v[0: a + i]) / (a + i)
m = max(s)
ans = 0
for i in range(c):
    if s[i] == m:
        r = v[0: a + i].count(v[a + i - 1])
        l = v.count(v[a + i - 1])
        ans += comb(l, min(r, l - r))
print(m)
print(ans)
