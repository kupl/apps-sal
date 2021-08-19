(n, d) = list(map(int, input().split()))
m = int(input())
for i in range(m):
    (x, y) = list(map(int, input().split()))
    if y <= x + d and y >= x - d and (y >= d - x) and (y <= 2 * n - d - x):
        print('YES')
    else:
        print('NO')
