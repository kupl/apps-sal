(a, b, c, d) = list(map(int, input().split()))
k = max(a, b, c, d)
z = min(a, b, c, d)
if k + z == a + b + c + d - k - z:
    print('YES')
elif k == a + b + c + d - k:
    print('YES')
else:
    print('NO')
