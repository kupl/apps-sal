import sys
e = int(input())
for ee in range(e):
    x, n, m = map(int, input().split())
    # a = [int(i) for i in input().split(' ', n - 1)]
    for i in range(n):
        y = x
        x = (x // 2) + 10
        if y < x:
            x = y
            break
    for i in range(m):
        x -= 10
    if x <= 0:
        print('YES')
    else:
        print('NO')
