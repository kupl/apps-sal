n, s = list(map(int, input().split(' ')))
if n <= s:
    ans = n
else:
    ans = s
    l = 0
    r = 10 ** 10
    n -= s
    while l + 1 < r:
        m = (l + r) // 2
        if m * (m + 1) // 2 < n:
            l = m
        else:
            r = m
    ans += r
print(ans)
