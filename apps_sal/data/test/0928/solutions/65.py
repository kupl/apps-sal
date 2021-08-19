import itertools
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
c = itertools.accumulate(a)
(ans, s, j) = (0, 0, 0)
for (i, v) in enumerate(c):
    while v - s >= k:
        ans += n - i
        s += a[j]
        j += 1
print(ans)
