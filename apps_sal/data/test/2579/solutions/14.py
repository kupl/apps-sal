(l, r, x, y, k) = list(map(int, input().split()))
a = max(k * x, l)
b = min(k * y, r)
a = (a + k - 1) // k
b = b // k
if a <= b:
    print('YES')
else:
    print('NO')
