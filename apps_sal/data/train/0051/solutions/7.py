def f(x, y, a, b): return x > a or y > b or (a - x) % 3 or (b - y) % 3
def g(x, y, a, b): return f(x, y, a, b) and f(x, y, b, a)
for i in range(int(input())):
    n, u, a, b = map(int, input().split())
    v, s, t = n - u, a + b, 2 * b - a if b > a else 2 * a - b
    print('no' if g(s, t, u, v) and g(s + a, s + b, u, v) else 'yes')
