(n, m) = list(map(int, input().split()))
(q, r) = divmod(n, m)
print((str(q + 1) + ' ') * r, (str(q) + ' ') * (m - r))
