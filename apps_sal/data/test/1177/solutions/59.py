n, s = map(int, input().split())
a = list(map(int, input().split()))
c = [0] * (s + 1)
ans = 0
mod = 998244353
for i in range(n):
    c_ = c.copy()
    if a[i] <= s:
        for j in range(a[i], s + 1):
            c[j] += c_[j - a[i]]
        c[a[i]] += i + 1
    ans += c[s]
    ans %= mod

print(ans)
