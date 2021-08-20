(n, x) = map(int, input().split())
if x == sum([int(x) for x in input().split()]) + n - 1:
    print('YES')
else:
    print('NO')
