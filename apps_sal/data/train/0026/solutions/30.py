t = int(input())
for u in range(t):
    (n, m) = list(map(int, input().split()))
    x = 2 * n + 2 * m
    y = 3 * n * m
    z = n * m
    if x + z >= y:
        print('YES')
    else:
        print('NO')
