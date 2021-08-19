(n, k) = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))
s = [0] * (n - k + 1)
res = 0
for i in range(n):
    if t[i] == 1:
        res += a[i]
for i in range(k):
    if t[i] == 0:
        s[0] += a[i]
for i in range(1, n - k + 1):
    w = 0
    if t[i - 1] == 0:
        w -= a[i - 1]
    if t[i + k - 1] == 0:
        w += a[i + k - 1]
    s[i] = s[i - 1] + w
print(res + max(s))
