(n, m) = list(map(int, input().split()))
now = 0
(am, bm) = (0, 0)
(l, r) = (-100000, 0)
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if l <= a <= r:
        l = min(a, abs(l))
        r = max(b, r)
if l != 0:
    print('NO')
elif l <= m <= r:
    print('YES')
else:
    print('NO')
