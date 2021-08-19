(n, k) = list(map(int, input().split()))
l = [None] * k
r = [None] * k
for i in range(k):
    (l[i], r[i]) = list(map(int, input().split()))
mod = 998244353
s = [0] * n
d = [0] * n
s[0] = 1
for i in range(n - 1):
    for j in range(k):
        if i + l[j] < n:
            d[i + l[j]] += s[i]
            d[i + l[j]] %= mod
        if i + r[j] + 1 < n:
            d[i + r[j] + 1] -= s[i]
            d[i + r[j] + 1] %= mod
    s[i + 1] = s[i] + d[i + 1]
    s[i + 1] %= mod
print(d[n - 1])
