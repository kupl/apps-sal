(l, r, x, y, k) = map(int, input().split())
if l % k != 0:
    l -= l % k
    l += k
r -= r % k
l //= k
r //= k
if max(l, x) <= min(r, y):
    print('YES')
else:
    print('NO')
