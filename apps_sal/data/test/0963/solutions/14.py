(n, k) = list(map(int, input().split()))
mod = 998244353
lr = []
a = [0] * (n + 1)
a[1] = 1
for _ in range(k):
    (l, r) = list(map(int, input().split()))
    lr.append([l, r])
for i in range(2, n + 1):
    for (l, r) in lr:
        if i - l < 0:
            continue
        a[i] += a[i - l] - a[max(0, i - r - 1)]
    a[i] += a[i - 1]
    a[i] %= mod
print((a[n] - a[n - 1]) % mod)
