n, m = [int(i) for i in input().split()]
mn = 10 ** 5
mx = 1
n -= 1
for i in range(m):
    x, y = [int(i) for i in input().split()]
    x -= 1
    y -= 1
    if y != 0:
        mn = min(mn, x // y)
    mx = max(mx, [(x + y) // (y + 1), x // (y + 1) + 1][x % (y + 1) == 0])
a = n // mx
for i in range(mx + 1, mn + 1):
    if a != n // i:
        print(-1)
        return
print(a + 1)
