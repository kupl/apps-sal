a, b, c = [int(s) for s in input().split()]
if (10 * b + c) % 4 == 0:
    print('YES')
else:
    print('NO')
