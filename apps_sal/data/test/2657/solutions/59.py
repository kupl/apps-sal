import bisect
_ = input()
a = [int(i) for i in input().split()]
a.sort()
n = a[-1]
m = n / 2
b = bisect.bisect(a, m)
s = a[b - 1]
t = a[b]
if m - s <= t - m:
    print(n, s)
else:
    print(n, t)
