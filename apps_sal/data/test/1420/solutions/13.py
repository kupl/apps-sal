__author__ = 'Rakshak.R.Hegde'
(n, l) = map(int, input().split())
a = sorted(map(int, input().split()))
r = 0.0
for i in range(n - 1):
    r = max(r, (a[i + 1] - a[i]) / 2.0)
r = max(r, a[0], l - a[-1])
print(r)
