n = int(input())
a, b, c, d = -10**9, 10**9, -10**9, 10**9
for _ in range(n):
    x, y = map(int, input().split())
    a = max(a, x + y)
    b = min(b, x + y)
    c = max(c, x - y)
    d = min(d, x - y)
print(max(a - b, c - d))
