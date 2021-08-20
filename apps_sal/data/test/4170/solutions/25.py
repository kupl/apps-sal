from itertools import groupby
n = int(input())
a = list(map(int, input().split()))
b = [0] * (n - 1)
for i in range(n - 1):
    if a[i] >= a[i + 1]:
        b[i] = 1
gr = groupby(b)
ans = 0
for (k, v) in gr:
    if k == 1:
        ans = max(ans, len(list(v)))
print(ans)
