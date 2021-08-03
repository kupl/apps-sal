n = int(input())
a, b, c, d = 2 * 10**9, 0, 10**9, -10**9

for i in range(n):
    x, y = list(map(int, input().split()))
    a = min(a, x + y)
    b = max(b, x + y)
    c = min(c, y - x)
    d = max(d, y - x)

print((max(b - a, d - c)))
