(n, d) = [int(i) for i in input().split()]
m = int(input())
for i in range(m):
    (x, y) = [int(i) for i in input().split()]
    if y <= x + d and y <= -1 * x + n - d + n and (y >= x - d) and (y >= -1 * x + d):
        print('YES')
    else:
        print('NO')
