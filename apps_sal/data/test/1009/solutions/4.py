(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
t = k - (2 * k - n)
res = 0
for i in range(t):
    res = max(res, a[i] + a[2 * t - 1 - i])
res = max(res, a[n - 1])
print(res)
