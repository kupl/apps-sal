n, m = map(int, input().split())
if (abs(n - m) <= 1 and not(n == 0 and m == 0)):
    print('YES')
else:
    print('NO')
