(n, l, r) = map(int, input().split())
mx = 1 << r
mx -= 1
mx += (1 << r - 1) * (n - r)
mn = 0
mn = 1 << l
mn -= 1
mn += n - l
print(mn, mx)
