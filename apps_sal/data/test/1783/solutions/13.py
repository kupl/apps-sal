(n, k) = list(map(int, input().split()))
ans = 0
a = list(map(int, input().split()))
s = sum(a[:k])
t = s
for i in range(1, 1 + n - k):
    s -= a[i - 1]
    s += a[i + k - 1]
    t += s
print(t / (1 + n - k))
