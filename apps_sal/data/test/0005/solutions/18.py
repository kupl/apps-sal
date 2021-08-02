def f(a, b, l, r, i):
    if a == l and b == r:
        return 0
    elif a == l and b > r:
        return 1 + abs(i - r)
    elif a < l and b == r:
        return 1 + abs(i - l)
    elif a < l and b > r:
        return 2 + abs(l - r) + min(abs(i - l), abs(i - r))


n, p, l, r = list(map(int, input().split()))
a, b = 1, n
t = 0

print(f(a, b, l, r, p))
