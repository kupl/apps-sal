n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
t = list(map(int, input().split()))

s = sum([a[i] * t[i] for i in range(n)])
s += sum([a[i] * (1 - t[i]) for i in range(k)])
ans = s
for i in range(n - k):
    s -= a[i] * (1 - t[i])
    s += a[i + k] * (1 - t[i + k])
    ans = max(ans, s)
print(ans)

