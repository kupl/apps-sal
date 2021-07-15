n, m, k = list(map(int, input().split()))
if k < n:
    r = [k + 1, 1]
else:
    m -= 1
    k -= n
    y, x = divmod(k, m)
    r = [n - y, 0]
    if y & 1:
        r[1] = m - x + 1
    else:
        r[1] = x + 2
print(*r)

