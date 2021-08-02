import math

n = int(input())
a = list(map(int, input().split()))
d = a[1] - a[0]
ok = True
for i in range(1, n):
    ok &= d == a[i] - a[i - 1]
print(a[n - 1] + d if ok else a[n - 1])
