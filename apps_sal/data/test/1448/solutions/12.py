(n, d) = [int(x) for x in input().split()]
m = int(input())
cnt = 0
for i in range(m):
    (x, y) = [int(x) for x in input().split()]
    if -x + d <= y <= -x + 2 * (n - d) + d and x - d <= y <= x + d:
        print('YES')
    else:
        print('NO')
