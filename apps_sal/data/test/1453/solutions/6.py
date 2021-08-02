from collections import defaultdict
n, m = map(int, input().split())
l = sorted(map(int, input().split()))
res = [0] * n
d = defaultdict(int)
for i in range(n):
    d[i % m] += l[i]
    res[i] += d[i % m]
    if i > 0: res[i] += res[i - 1]
print(*res)
