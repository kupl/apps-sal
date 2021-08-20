(n, l, r) = map(int, input().split())
mn = (1 << l) - 1 + (n - l)
mx = (1 << r) - 1 + (n - r) * (1 << r - 1)
print(mn, mx)
