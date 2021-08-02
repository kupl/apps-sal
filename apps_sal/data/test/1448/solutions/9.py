
n, d = (int(e) for e in input().split(' '))

for i in range(int(input())):
    x, y = (int(e) for e in input().split(' '))
    d1, d2 = x - y, x + y
    if(-d <= d1 <= d and d <= d2 <= n - d + n):
        print('YES')
    else:
        print('NO')

"""
7 2
4
2 4
4 1
6 3
4 5

YES
NO
NO
YES

"""
