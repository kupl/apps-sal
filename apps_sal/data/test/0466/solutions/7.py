def f(x, y): return x * c + y * d


c, d = map(int, input().split())
n, m = map(int, input().split())
k = n * m - int(input())
x, s = 0, max(0, k * d)
while k > x * n:
    t = f(x, k - x * n)
    if t < s: s = t
    x += 1
print(min(s, f(x, 0)))
