(n, l, r) = map(int, input().split())
mn = n - l + 2 ** l - 1
mx = (n - r) * 2 ** (r - 1) + 2 ** r - 1
print(*[mn, mx])
