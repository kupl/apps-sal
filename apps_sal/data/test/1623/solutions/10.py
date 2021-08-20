(n, l, r) = list(map(int, input().split()))
forced = 2 ** l - 1
mn = forced + n - l
if r > n:
    r = n
forced = 2 ** r - 1
mx = forced + 2 ** (r - 1) * (n - r)
print(mn, mx)
