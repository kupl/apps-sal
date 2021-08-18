
def nC2(n):
    return n * (n - 1) // 2


SIZE = 1000

N = int(input())
a = [[0] * SIZE for i in range(SIZE)]
for i in range(N):
    x, y = map(int, input().split())
    a[x - 1][y - 1] = 1

ans = 0

for sx in range(SIZE):
    t_cnt = 0

    x = sx
    y = 0
    while x >= 0:
        t_cnt += a[x][y]
        x -= 1
        y += 1

    ans += nC2(t_cnt)

for sy in range(1, SIZE):
    t_cnt = 0

    x = SIZE - 1
    y = sy
    while y < SIZE:
        t_cnt += a[x][y]
        x -= 1
        y += 1

    ans += nC2(t_cnt)

for sx in range(SIZE):
    t_cnt = 0

    x = sx
    y = 0
    while x < SIZE:
        t_cnt += a[x][y]
        x += 1
        y += 1

    ans += nC2(t_cnt)

for sy in range(1, SIZE):
    t_cnt = 0

    x = 0
    y = sy
    while y < SIZE:
        t_cnt += a[x][y]
        x += 1
        y += 1

    ans += nC2(t_cnt)

print(ans)
