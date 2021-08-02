n, s = map(int, input().split())
t = [0] * (s + 1)
m = 998244353
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    d = t.copy()
    if a[i] <= s:
        for j in range(a[i], s + 1):
            t[j] += d[j - a[i]]
        t[a[i]] += i + 1
    ans += t[-1]
    ans %= m
print(int(ans))
