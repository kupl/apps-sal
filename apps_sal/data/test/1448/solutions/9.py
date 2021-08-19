(n, d) = (int(e) for e in input().split(' '))
for i in range(int(input())):
    (x, y) = (int(e) for e in input().split(' '))
    (d1, d2) = (x - y, x + y)
    if -d <= d1 <= d and d <= d2 <= n - d + n:
        print('YES')
    else:
        print('NO')
'\n7 2\n4\n2 4\n4 1\n6 3\n4 5\n\nYES\nNO\nNO\nYES\n\n'
