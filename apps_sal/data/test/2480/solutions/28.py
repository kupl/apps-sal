from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
a[0] = (a[0] - 1) % k
for i in range(n - 1):
    a[i + 1] = (a[i + 1] + a[i] - 1) % k
d = defaultdict(int)
ans = 0
d[0] = 1
for i in range(n):
    if i == k - 1:
        d[0] -= 1
    if i >= k:
        d[a[i - k]] -= 1
    ans += d[a[i]]
    d[a[i]] += 1
print(ans)
