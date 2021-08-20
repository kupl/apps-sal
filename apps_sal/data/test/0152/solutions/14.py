import bisect
((n, m, k), (x, s), a, b, c, d) = (list(map(int, input().split())) for _ in range(6))
(a, b) = (list(a) + [x], list(b) + [0])
(c, d) = list(map(list, (c, d)))
ans = n * x
for i in range(m + 1):
    if b[i] <= s:
        j = bisect.bisect_right(d, s - b[i])
        if j > 0:
            j -= 1
            ans = min(ans, (n - c[j]) * a[i])
        else:
            ans = min(ans, n * a[i])
print(ans)
