from bisect import bisect_left
(n, m, x, *a) = list(map(int, open(0).read().split()))
b = bisect_left(a, x)
print(min(m - b, b))
