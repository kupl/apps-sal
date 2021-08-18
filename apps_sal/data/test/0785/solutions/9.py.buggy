n, a, b = map(int, input().split())
n = 6 * n
s = a * b
if s >= n:
    print(s)
    print(a, b)
    return
m = int(n ** 0.5) + 1
s = (a + m) * (b + m)
for x in range(a, m):
    y = max((n - 1) // x + 1, b)
    if x * y < s:
        s = x * y
        u, v = x, y
for y in range(b, m):
    x = max((n - 1) // y + 1, a)
    if x * y < s:
        s = x * y
        u, v = x, y
print(s)
print(u, v)
