read = lambda: list(map(int, input().split()))
f = lambda x, y, a, b: x > a or y > b or (a - x) % 3 or (b - y) % 3
g = lambda x, y, a, b: f(x, y, a, b) and f(x, y, b, a)
t = int(input())
for i in range(t):
    n, k, d1, d2 = read()
    r = n - k
    d = d1 + d2
    p = 2 * d2 - d1 if d2 > d1 else 2 * d1 - d2
    print('no' if g(d, p, k, r) and g(d + d1, d + d2, k, r) else 'yes')

