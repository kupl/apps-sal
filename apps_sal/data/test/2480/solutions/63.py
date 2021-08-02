from collections import defaultdict
n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
d = defaultdict(int)
d[0] = 1
ans = 0
for i in range(1, n + 1):
    a[i] += a[i - 1] - 1
    if i >= k:
        d[a[i - k]] -= 1
    a[i] %= k
    d[a[i]] += 1
    ans += d[a[i]] - 1
print(ans)
