from itertools import accumulate, islice
from bisect import bisect_left
n = int(input())
xs = list(map(int, input().split()))
ys = list(accumulate(xs))
(zs, total) = (ys[:-1], ys[-1])
res = max(xs) - min(xs)
for (i, z) in islice(enumerate(zs), 1, n - 1):
    j = bisect_left(zs, z // 2)
    splits = ((zs[j + k], z - zs[j + k]) for k in (-1, 0, 1) if 0 <= j + k <= i)
    (a, b) = min(splits, key=lambda s: abs(s[0] - s[1]))
    j = bisect_left(zs, (total - z) // 2 + z)
    splits = ((zs[j + k] - z, total - zs[j + k]) for k in (-1, 0, 1) if i <= j + k <= n - 2)
    (c, d) = min(splits, key=lambda s: abs(s[0] - s[1]))
    (minn, _, _, maxx) = sorted((a, b, c, d))
    if maxx - minn < res:
        res = maxx - minn
print(res)
