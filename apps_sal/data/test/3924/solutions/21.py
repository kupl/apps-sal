from math import ceil

n, k = tuple(map(int, input().split()))
a = list(map(int, input().split()))
s = 0
r = 0
for i in range(n - 1, -1, -1):
    a[i] = max(0, a[i] - r)
    s += int(ceil(a[i] / k))
    if (a[i] % k) != 0:
        r = k - (a[i] % k)
    else:
        r = 0
print(s)
