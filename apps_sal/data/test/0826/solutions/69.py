def bisect(item, l, r):
    if r - l == 1:
        return l + 1
    m = l + (r - l) // 2
    if m * (m + 1) > item:
        return bisect(item, l, m)
    else:
        return bisect(item, m, r)


n = int(input())
m = bisect(2 * (n + 1), 0, n + 1) - 1
print(n + 1 - m)
