from collections import defaultdict
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
d = defaultdict(int)
sa = [0] * (n + 1)
for i in range(n):
    sa[i + 1] = sa[i] + a[i]
    sa[i + 1] %= k
ans = 0
for i in range(n + 1):
    v = sa[i] - i
    v %= k
    ans += d[v]
    d[v] += 1
    if 0 <= i - k + 1:
        vv = sa[i - k + 1] - (i - k + 1)
        vv %= k
        d[vv] -= 1
print(ans)
