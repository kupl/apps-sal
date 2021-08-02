n, k = list(map(int, input().split()))
p = 998244353
l = []
r = []

for i in range(0, k):
    x, y = list(map(int, input().split()))
    l.append(x)
    r.append(y)

a = [0] * (n + 1)
s = [0] * (n + 1)
a[1] = 1
s[1] = 1

for i in range(2, n + 1):
    for j in range(0, k):
        L = max(i - r[j], 1)
        R = max(i - l[j], 0)
        a[i] += s[R] - s[L - 1]
        a[i] %= p
    s[i] = s[i - 1] + a[i]
    s[i] %= p

print((a[n]))
