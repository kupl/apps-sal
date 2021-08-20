(n, m, k) = list(map(int, input().split()))
(r, c) = (None, None)
if k < n:
    (r, c) = (k + 1, 1)
else:
    k -= n
    (a, b) = (k // (m - 1), k % (m - 1))
    r = n - a
    if a % 2 == 0:
        c = b + 2
    else:
        c = m - b
print(r, c)
