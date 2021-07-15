x, y = 0, 0
n = int(input())
for _ in range(2*n):
    a, b = map(int, input().strip().split())
    x += a
    y += b
print(x // n, y // n)
