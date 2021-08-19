from collections import defaultdict
(n, x, d) = list(map(int, input().split()))
if d == 0:
    if x == 0:
        ans = 1
    else:
        ans = n + 1
else:
    if d < 0:
        (x, d) = (-x, -d)
    intervals = defaultdict(list)
    for i in range(n + 1):
        l = i * (i - 1) // 2
        r = i * (2 * n - i - 1) // 2
        a = x * i % d
        b = x * i // d
        intervals[a].append((l + b, r + b))
    ans = 0
    for interval in list(intervals.values()):
        interval.sort()
        (l, r) = interval[0]
        ans += r - l + 1
        for i in range(1, len(interval)):
            (li, ri) = interval[i]
            if ri <= r:
                continue
            elif li <= r:
                ans += ri - (r + 1) + 1
                (l, r) = (li, ri)
            else:
                ans += ri - li + 1
                (l, r) = (li, ri)
print(ans)
