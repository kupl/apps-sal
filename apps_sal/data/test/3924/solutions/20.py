(n, k) = list(map(int, input().split()))
a = list(map(int, input().split())) + [0]
ans = 0
r = 0
for i in range(n - 1, -1, -1):
    s = a[i]
    s = max(0, a[i] - r)
    x = (s + k - 1) // k
    ans += x
    r = x * k - s
print(ans)
