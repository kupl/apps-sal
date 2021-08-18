from bisect import bisect_left

n, x, k = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))

ranges = []
for a in arr:
    if k == 0:
        a1 = (((a - 1) // x) + 1) * x
        l = a
        r = a1 + x * (k - 1) + x
    else:
        a1 = (((a - 1) // x) + 1) * x
        l = a1 + x * (k - 1)
        r = a1 + x * (k - 1) + x
    ranges.append((min(l, r), max(l, r)))
res = 0


for l, r in ranges:
    left_index = bisect_left(arr, l)
    right_index = bisect_left(arr, r)
    res += right_index - left_index

print(res)
