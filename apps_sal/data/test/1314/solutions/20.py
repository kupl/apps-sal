n = int(input())
(x, y) = (0, 0)
for i in range(2 * n):
    (a, b) = list(map(int, input().split()))
    x += a
    y += b
print(x // n, y // n)
