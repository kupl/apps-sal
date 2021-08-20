(n, x) = map(int, input().split())
if n == 1:
    print('YES')
    print(x)
elif n == 2:
    if x:
        print('YES\n0', x)
    else:
        print('NO')
else:
    print('YES')
    y = 0
    p = 1 << 17
    for i in range(1, n - 2):
        print(i, end=' ')
        y ^= i
    if y - x:
        print(0, p, p ^ x ^ y)
    else:
        print(p, p * 2, p ^ p * 2)
