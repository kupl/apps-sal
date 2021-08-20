n = int(input())
(x, y) = (0, 0)
for _ in range(2 * n):
    (dx, dy) = map(int, input().split())
    x += dx
    y += dy
print(x // n, y // n)
